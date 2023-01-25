## Espanso package for Lean input abbreviations

This repository contains a configuration file
for the [Espanso](https://espanso.org/) text expansion tool.
It allows you to use Lean input abbreviations
like `\all `
system-wide, in any program.
The list of abbreviations is taken from the canonical source,
the [Lean 4 VS Code extension](https://github.com/leanprover/vscode-lean4/blob/master/vscode-lean4/src/abbreviation/abbreviations.json).

Please note that the behavior of the espanso expansions
is slightly different from how the editor plugins work:
you need to type a space after every abbreviation.

How to use:
```bash
cp lean.yml `espanso path config`/match
```

See also [`m17n-lean`](https://github.com/gebner/m17n-lean)
for a similar set-up using input methods.

### Disable espanso in VS Code
To disable espanso in certain apps like VS Code you can add a config
file `[espanso path config]/match/code.yml` with the following content:

```
filter_title: Visual Studio Code
enable: false
```

See [Espanso docs](https://espanso.org/docs/configuration/app-specific-configurations/).
