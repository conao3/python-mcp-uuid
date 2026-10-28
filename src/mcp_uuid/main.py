import uuid
from mcp.server.mcpserver import MCPServer

app = MCPServer("mcp-uuid")

@app.tool()
def action_uuid() -> str:
    return str(uuid.uuid4())

def main():
    app.run()

if __name__ == '__main__':
    main()
