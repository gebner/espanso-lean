## Espanso package for Lean input abbreviations

This repository contains a configuration file
for the [Espanso](https://espanso.org/) text expansion tool.
It allows you to use Lean input abbreviations
like `\all`
system-wide, in any program.
The list of abbreviations is taken from the canonical source,
the [Lean 4 VS Code extension](https://github.com/leanprover/vscode-lean4/blob/master/vscode-lean4/src/abbreviation/abbreviations.json).

See also [`m17n-lean`](https://github.com/gebner/m17n-lean)
for a similar set-up using input methods.

How to use:
```bash
cp lean.yml `espanso path config`/match
```
