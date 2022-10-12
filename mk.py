import yaml, json

with open('abbreviations.json') as f:
    abbrs = json.load(f)

leader = '\\'

matches = []
for abbr, repl in abbrs.items():
    if '$CURSOR' in repl: continue
    trigger = leader + abbr
    # We require a space after abbreviations for disambiguation.
    # Otherwise `\exists` would expand to `εxists`.
    trigger += ' '
    matches.append({
        'trigger': trigger,
        'replace': repl,
    })

with open('lean.yml', 'w') as f:
    yaml.dump({'matches': matches}, f)
