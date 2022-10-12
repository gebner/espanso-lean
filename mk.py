import yaml, json

with open('abbreviations.json') as f:
    abbrs = json.load(f)

leader = '\\'

# Espanso only replaces full matches,
# so add all prefixes:
for abbr, repl in list(abbrs.items()):
    abbr = abbr[:-1]
    while abbr != '' and abbr not in abbrs:
        abbrs[abbr] = repl
        abbr = abbr[:-1]

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
