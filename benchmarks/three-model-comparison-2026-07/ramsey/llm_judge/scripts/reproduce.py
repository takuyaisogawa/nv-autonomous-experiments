"""Verify archived inputs/labels and reproduce judge counts and human agreement."""
from pathlib import Path
from collections import Counter, defaultdict
import csv
import hashlib
import json
import math
import random

ROOT = Path(__file__).resolve().parents[1]

def read(path): return json.loads(path.read_text(encoding='utf-8'))
def records(path): return [json.loads(s) for s in path.read_text(encoding='utf-8').splitlines() if s.strip()]
def digest(data): return hashlib.sha256(data).hexdigest()
def save(path, data): path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def agreement(a,b):
    n=len(a); matrix=Counter(zip(a,b)); observed=sum(x==y for x,y in zip(a,b))/n
    expected=sum(a.count(v)*b.count(v) for v in ['PASS','FAIL'])/(n*n)
    z=1.959963984540054; denominator=1+z*z/n
    center=(observed+z*z/(2*n))/denominator
    half=z*math.sqrt(observed*(1-observed)/n+z*z/(4*n*n))/denominator
    return {'n':n,'agreement_count':round(observed*n),'agreement_rate':observed,
            'cohen_kappa':(observed-expected)/(1-expected) if expected<1 else None,
            'agreement_wilson_95ci':[center-half,center+half],
            'confusion_matrix':{f'{x}_{y}':matrix[(x,y)] for x in ['PASS','FAIL'] for y in ['PASS','FAIL']}}

def main():
    if (ROOT/'checksums.json').exists():
        for name,expected in read(ROOT/'checksums.json').items():
            assert digest((ROOT/name).read_bytes())==expected, f'Changed frozen file: {name}'
    inputs={x['case_id']:x['input'] for x in records(ROOT/'inputs.jsonl')}
    judges={x['case_id']:x for x in records(ROOT/'judgments.jsonl')}
    mapping={x['case_id']:x for x in records(ROOT/'case_mapping.jsonl')}
    legacy={x['case_id']:x for x in records(ROOT/'legacy_comparison/previous_scores.jsonl')}
    checks={x['case_id']:x for x in records(ROOT/'execution_checks.jsonl')}
    assert len(inputs)==1200 and inputs.keys()==judges.keys()==mapping.keys()==legacy.keys()==checks.keys()
    guide=(ROOT/'prompts/scoring_guide.md').read_text(encoding='utf-8')
    prompt=(ROOT/'prompts/judge_prompt.txt').read_text(encoding='utf-8')
    assert prompt.split('Scoring guide:\n',1)[1]==guide
    quote_flags=[]
    for entry in read(ROOT/'input_manifest.json'):
        cid=entry['case_id']; inp=inputs[cid]
        assert set(inp)=={'original_task_prompt','final_response','project_note'}
        canonical=json.dumps(inp,ensure_ascii=False,indent=2)+'\n'
        assert digest(canonical.encode('utf-8'))==entry['input_sha256'],cid
        for field in ['final_response','project_note']:
            assert digest(inp[field].encode('utf-8'))==entry[field+'_sha256'], (cid,field)
        payload=prompt.rstrip()+'\n\n'+(
            'The JSON below contains the original task (context only) and the complete texts to grade.\n'
            'Only final_response and project_note may be quoted as evidence.\n\n')+canonical
        assert digest(payload.encode('utf-8'))==checks[cid]['payload_sha256'],cid
        for evidence in judges[cid]['evidence']:
            if evidence['quote'] not in inp[evidence['source']]:
                quote_flags.append({'case_id':cid,**evidence,
                    'case_insensitive_match':evidence['quote'].lower() in inp[evidence['source']].lower()})
    assert len(quote_flags)==1 and quote_flags[0]['case_id']=='case0010' and quote_flags[0]['case_insensitive_match']
    assert checks['case0010']['status']=='review_required'
    selection=read(ROOT/'human_validation_100/selection.json')
    pool=sorted(set(inputs)-set(selection['excluded_pilot_ids']))
    assert len(pool)==1184 and len(selection['excluded_pilot_ids'])==16
    sampled=random.Random(selection['seed']).sample(pool,100)
    assert sampled==[r['source_case_id'] for r in selection['cases']]
    original=read(ROOT/'human_validation_100/human_original.json')
    hr=original['records']
    human_comparison=read(ROOT/'human_validation_100/comparison.json')
    assert digest((ROOT/'human_validation_100/human_original.json').read_bytes())==human_comparison['human_export_sha256']
    hvals=[]; jvals=[]
    for row in human_comparison['cases']:
        h=hr[row['review_id']]
        assert h['verdict']==row['human_verdict'] and h['reason']==row['human_reason']
        assert judges[row['source_case_id']]['verdict']==row['judge_verdict']
        hvals.append(row['human_verdict']); jvals.append(row['judge_verdict'])
    human=agreement(hvals,jvals)
    assert human['agreement_count']==96 and abs(human['cohen_kappa']-human_comparison['cohen_kappa'])<1e-12
    assert all(abs(x-y)<1e-12 for x,y in zip(human['agreement_wilson_95ci'],human_comparison['agreement_wilson_95ci']))
    buckets=defaultdict(list)
    for cid,meta in mapping.items():
        buckets[(meta['model'],meta['reasoning_effort'],meta['checkpoint_id'])].append(judges[cid]['verdict'])
    assert len(buckets)==60 and all(len(v)==20 for v in buckets.values())
    rows=[{'model':m,'reasoning_effort':e,'checkpoint_id':c,'passes':v.count('PASS'),'total':len(v)} for (m,e,c),v in sorted(buckets.items())]
    assert sum(r['passes'] for r in rows)==269
    expected_counts={'gpt-5.4':[7,10,16,22],'gpt-5.5':[4,17,18,27],'gpt-5.6-sol':[15,36,53,44]}
    counts={m:[sum(r['passes'] for r in rows if r['model']==m and r['reasoning_effort']==e) for e in ['low','medium','high','xhigh']] for m in expected_counts}
    assert counts==expected_counts
    ids=sorted(inputs); old=agreement([legacy[i]['verdict'] for i in ids],[judges[i]['verdict'] for i in ids])
    assert old['agreement_count']==1147 and old['confusion_matrix']['PASS_FAIL']==43 and old['confusion_matrix']['FAIL_PASS']==10
    destination=ROOT/'reproduced'; destination.mkdir(exist_ok=True)
    save(destination/'human_agreement.json',human)
    save(destination/'previous_score_agreement.json',old)
    save(destination/'quote_validation.json',quote_flags)
    with (destination/'checkpoint_counts.csv').open('w',encoding='utf-8',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    print(json.dumps({'responses':len(inputs),'judge_PASS':269,'human_agreement':human,
                      'previous_score_agreement':old['agreement_count'],'pass_counts':counts,
                      'original_capitalization_only_quote_flags':len(quote_flags),'sample_reproduced':True},indent=2))

if __name__=='__main__': main()
