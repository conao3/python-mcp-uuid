# mcp-uuid

A Model Context Protocol (MCP) server that provides UUID generation capabilities. This lightweight server exposes a simple tool for generating random UUIDs (v4) that can be used by MCP-compatible clients like Claude Desktop.

## Requirements

- Python 3.13 or higher
- [PDM](https://pdm-project.org/) package manager

## Installation

Install the package and create a symlink to make the command globally available:

```bash
pdm install
ln -s $(pdm run which mcp-uuid) ~/.local/bin/
```

Make sure `~/.local/bin` is in your PATH. Add the following to your shell configuration file (e.g., `.bashrc` or `.zshrc`) if needed:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

## Configuration

### Claude Desktop

Add the following to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "uuid": {
      "command": "mcp-uuid"
    }
  }
}
```

## Development

Run the server in development mode:

```bash
pdm run mcp-uuid
```

## NixOS Notes

### Virtual Environment Backend

PDM uses `virtualenv` by default, which may not be available on NixOS-managed Python installations. Configure PDM to use the built-in `venv` module instead:

```bash
pdm config venv.backend venv
```

See [NixOS/nixpkgs#225730](https://github.com/NixOS/nixpkgs/issues/225730) for more details.

## License

See [LICENSE](LICENSE) for details.
