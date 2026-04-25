from blender_mcp.server import main as server_main
import sys

def main():
    """Entry point for the blender-mcp package.
    
    Runs the MCP server that connects Blender to AI assistants via the
    Model Context Protocol. Start Blender first before running this.
    """
    server_main()

if __name__ == "__main__":
    main()
