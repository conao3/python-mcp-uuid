import uuid
import mcp.server.fastmcp

app = mcp.server.fastmcp.FastMCP("mcp-uuid")

@app.tool()
def action_uuid() -> str:
    return str(uuid.uuid4())

def main():
    app.run()

if __name__ == '__main__':
    main()
