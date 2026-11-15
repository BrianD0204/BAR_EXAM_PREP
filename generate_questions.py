"""Generate 280 original practice items from 140 reviewed legal-study concepts.
Two complementary questions per concept: identify a rule in a fact pattern, then
identify the correct explanation of that named rule. For supplemental practice only.
"""
import json, random, collections
from pathlib import Path
ROOT = Path(__file__).resolve().parent
raw = []
for line in (ROOT/'concepts.tsv').read_text(encoding='utf-8').splitlines():
    if not line or line.startswith('#'): continue
    bits = [part.strip() for part in line.split('::')]
    if len(bits) != 4: raise ValueError(f'Bad row: {line}')
    raw.append(dict(subject=bits[0], name=bits[1], scenario=bits[2], rule=bits[3]))
groups = collections.defaultdict(list)
for concept in raw: groups[concept['subject']].append(concept)
assert len(groups) == 7 and all(len(items) == 20 for items in groups.values()), 'Need 20 concepts for each of 7 MBE subjects'
rng = random.Random(20261114)
questions = []
for subject, concepts in groups.items():
    for index, concept in enumerate(concepts, 1):
        pool = [c for c in concepts if c is not concept]
        wrong = rng.sample(pool, 3)
        for suffix in ('A','B'):
            if suffix == 'A':
                prompt = concept['scenario']
                correct = concept['name']
                distractors = [item['name'] for item in wrong]
            else:
                prompt = f"Which statement correctly describes {concept['name']}?"
                correct = concept['rule']
                distractors = [item['rule'] for item in wrong]
            options = [correct, *distractors]
            rng.shuffle(options)
            questions.append({
                'id': f"{''.join(x[0] for x in subject.split())}-{index:02d}-{suffix}",
                'subject': subject, 'topic': concept['name'], 'type': 'application' if suffix == 'A' else 'rule',
                'question': prompt, 'options': options, 'answer': options.index(correct),
                'explanation': f"{concept['name']}: {concept['rule']}",
            })
assert len(questions) == 280
(ROOT/'questions.json').write_text(json.dumps(questions, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
(ROOT/'questions.js').write_text('/* Original educational practice prompts; not licensed NCBE exam items. */\nwindow.BAR_QUESTIONS = '+json.dumps(questions, ensure_ascii=False, separators=(',',':'))+';\n', encoding='utf-8')
print(f"Generated {len(questions)} questions across {len(groups)} subjects")
