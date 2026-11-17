from mcp.server.mcpserver import MCPServer

mcp = MCPServer("test server")

@mcp.tool()
def code_word() -> str:
    """returns the universal code word."""
    return "bananas"

if __name__ == "__main__":
    mcp.run()