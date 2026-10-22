"""Run fresh judgments without reading or replacing any published labels."""
from pathlib import Path
import argparse
import hashlib
import json
import subprocess
import tempfile
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parents[1]

def load(p): return json.loads(p.read_text(encoding='utf-8'))

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    group=parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--case');group.add_argument('--all',action='store_true')
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--codex',default='codex')
    parser.add_argument('--prepare-only',action='store_true',help='Write payloads without making model calls')
    args=parser.parse_args()
    config=load(ROOT/'config.json')
    rows=[json.loads(s) for s in (ROOT/'inputs.jsonl').read_text(encoding='utf-8').splitlines()]
    selected=[r for r in rows if args.all or r['case_id']==args.case]
    if not selected: parser.error('Unknown case ID')
    args.output=args.output.resolve()
    args.output.mkdir(parents=True,exist_ok=False)
    if not args.prepare_only:
        version=subprocess.run([args.codex,'--version'],check=True,capture_output=True,text=True,encoding='utf-8').stdout.strip()
        if version!=config['expected_cli_version']:
            raise RuntimeError(f"Expected {config['expected_cli_version']}; found {version}. Install the recorded version to reproduce its setup.")
    for row in selected:
        source=row['input']; assert set(source)=={'original_task_prompt','final_response','project_note'}
        payload=(ROOT/'prompts/judge_prompt.txt').read_text(encoding='utf-8').rstrip()+'\n\n'+(
            'The JSON below contains the original task (context only) and the complete texts to grade.\n'
            'Only final_response and project_note may be quoted as evidence.\n\n')+json.dumps(source,ensure_ascii=False,indent=2)+'\n'
        output=args.output/row['case_id'];output.mkdir()
        (output/'input.txt').write_text(payload,encoding='utf-8',newline='\n')
        if args.prepare_only: continue
        with tempfile.TemporaryDirectory(prefix='ramsey-judge-') as tmp:
            folder=Path(tmp)
            for name in ['judge_instructions.txt','output_schema.json']:
                (folder/name).write_bytes((ROOT/'prompts'/name).read_bytes())
            cmd=[args.codex,'--no-daemon','-a','never','exec','--ignore-user-config','--ephemeral','--strict-config',
                '--skip-git-repo-check','--sandbox','read-only','--model',config['model'],'--cd',str(folder),
                '--color','never','--json','--output-schema',str(folder/'output_schema.json'),
                '--output-last-message',str(output/'result.json')]
            settings={'model_reasoning_effort':config['reasoning_effort'],
                'model_instructions_file':str(folder/'judge_instructions.txt'),
                'developer_instructions':'','project_doc_max_bytes':0,'web_search':'disabled','features.skip_host_skill_discovery':True}
            for key,value in settings.items(): cmd+=['-c',f'{key}={json.dumps(value)}']
            for feature in config['disabled_features']: cmd+=['--disable',feature]
            cmd+=['-']; started=datetime.now(timezone.utc).isoformat()
            with (output/'events.jsonl').open('wb') as stdout, (output/'stderr.txt').open('wb') as stderr:
                process=subprocess.run(cmd,input=payload.encode('utf-8'),stdout=stdout,stderr=stderr,timeout=config['timeout_seconds'])
            events=[json.loads(s) for s in (output/'events.jsonl').read_text(encoding='utf-8').splitlines() if s.strip()]
            forbidden={'command_execution','mcp_tool_call','web_search','file_change','function_call','custom_tool_call','tool_call','collab_tool_call'}
            def inspect(v):
                if isinstance(v,dict):
                    kind=str(v.get('type',''));assert kind not in forbidden and not kind.endswith('_tool_call'),kind
                    for x in v.values(): inspect(x)
                elif isinstance(v,list):
                    for x in v: inspect(x)
            inspect(events)
            assert process.returncode==0 and any(e.get('type')=='turn.completed' for e in events)
            result=load(output/'result.json')
            assert set(result)=={'verdict','evidence','justification','confidence'}
            assert result['verdict'] in ['PASS','FAIL'] and result['confidence'] in ['high','medium','low']
            quote_issues=[e for e in result['evidence'] if e['source'] not in source or e['quote'] not in source[e['source']]]
            record={'case_id':row['case_id'],'started_utc':started,'finished_utc':datetime.now(timezone.utc).isoformat(),
                'payload_sha256':hashlib.sha256(payload.encode('utf-8')).hexdigest(),'quote_issues':quote_issues}
            (output/'execution.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
        print(row['case_id'],result['verdict'])

if __name__=='__main__': main()
