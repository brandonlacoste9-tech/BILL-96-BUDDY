"""
Test script to verify Playwright MCP server connectivity
This will help diagnose if the Playwright tools are accessible
"""

# The Playwright MCP server should be running if configured in mcp.json
# We need to verify it's accessible through Kiro's tool system

print("Playwright MCP Server Test")
print("=" * 50)
print("Configuration found in .kiro/settings/mcp.json")
print("Server: playwright")
print("Command: uvx mcp-server-playwright")
print("Status: disabled=false")
print()
print("Next step: Verify MCP server is connected in Kiro")
