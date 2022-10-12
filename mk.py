import yaml, json

with open('abbreviations.json') as f:
    abbrs = json.load(f)

leader = '\\'

matches = []
for abbr, repl in abbrs.items():
    if '$CURSOR' in repl: continue
    matches.append({
        'trigger': leader + abbr,
        'replace': repl,
    })

with open('lean.yml', 'w') as f:
    yaml.dump({'matches': matches}, f)
