# python-mcp-uuid

# Usage
## Install
```bash
pdm install
```

# NixOS tips
## pdm fails missing virtualenv
`pdm` uses `virtualenv` to create virtual env but Python which installed by NixOS don't have it, pdm fails.

ref: https://github.com/NixOS/nixpkgs/issues/225730

```bash
pdm config venv.backend venv
```
