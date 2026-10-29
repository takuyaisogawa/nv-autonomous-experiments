"""Recompute Astra's bootstrap intervals from the released judgments."""
from pathlib import Path
import json
import numpy as np

ROOT = Path(__file__).resolve().parent
records = [json.loads(s) for s in (ROOT/'podmr/gpt-6-astra/responses.jsonl').read_text(encoding='utf-8').splitlines() if s.strip()]
saved = {(r['context_id'], r['reasoning_effort']): r for r in json.loads((ROOT/'data/podmr_summary.json').read_text(encoding='utf-8')) if r['model']=='GPT-6 Astra'}
efforts = ['low', 'medium', 'high', 'xhigh']
contexts = ['context_0', 'context_A', 'context_B']
assert len(records)==3456 and len(saved)==12

def interval(values, rng):
    values = np.asarray(values)
    return np.quantile(values[rng.integers(0, len(values), size=(20000, len(values)))].mean(axis=1), [.025, .975])

# The initial 864 judgments used a separate sequence of bootstrap draws.
# Retain those intervals exactly when completing the remaining conditions.
previous = {}
rng = np.random.default_rng(20261028)
for effort in efforts:
    group = [r for r in records if r['context_id']=='context_0' and r['reasoning_effort']==effort and r['gold_label']=='absent']
    ids = sorted({r['case_id'] for r in group})
    assert len(ids)==72
    values = [sum(r['outcome']=='FP' for r in group if r['case_id']==cid)/3 for cid in ids]
    previous[effort] = interval(values, rng)

rng = np.random.default_rng(20261028)
for context in contexts:
    for effort in efforts:
        group = [r for r in records if r['context_id']==context and r['reasoning_effort']==effort]
        ids = sorted({r['case_id'] for r in group})
        cases = [[r for r in group if r['case_id']==cid] for cid in ids]
        assert len(cases)==96 and all(len(g)==3 for g in cases)
        correct = [sum(r['outcome'] in ('TP', 'TN') for r in g)/3 for g in cases]
        absent = [g for g in cases if g[0]['gold_label']=='absent']
        false_positive = [sum(r['outcome']=='FP' for r in g)/3 for g in absent]
        accuracy_ci = interval(correct, rng)
        fpr_ci = interval(false_positive, rng)
        if context=='context_0':
            fpr_ci = previous[effort]
        row = saved[context, effort]
        for metric, actual in [('accuracy', accuracy_ci), ('false_positive_rate', fpr_ci)]:
            expected = [row[metric+'_ci_low'], row[metric+'_ci_high']]
            assert np.allclose(actual, expected, rtol=0, atol=1e-12), (context, effort, metric)
print(json.dumps({'verified_astra_conditions': 12, 'bootstrap_resamples': 20000, 'seed': 20261028, 'previous_sequence_intervals_retained': True}))
