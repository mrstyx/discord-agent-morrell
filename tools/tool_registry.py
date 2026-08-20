"""Tool registry and management system for the Discord Agent."""

from typing import Dict, Any, Callable, List
from utils.logger import setup_logger

logger = setup_logger(__name__)


class Tool:
    """Represents a single tool that the agent can use."""
    
    def __init__(
        self,
        name: str,
        description: str,
        func: Callable,
        parameters: Dict[str, Any] = None
    ):
        """Initialize a tool.
        
        Args:
            name: Tool name (used for agent to identify the tool)
            description: Human-readable description of what the tool does
            func: Async function that implements the tool
            parameters: Schema of parameters the tool accepts
        """
        self.name = name
        self.description = description
        self.func = func
        self.parameters = parameters or {}
    
    async def execute(self, **kwargs) -> Any:
        """Execute the tool with given parameters.
        
        Args:
            **kwargs: Tool parameters
        
        Returns:
            Tool execution result
        """
        return await self.func(**kwargs)
    
    def to_schema(self) -> Dict[str, Any]:
        """Convert tool to JSON schema for the agent.
        
        Returns:
            JSON schema representation of the tool
        """
        return {
            'name': self.name,
            'description': self.description,
            'parameters': self.parameters
        }


class ToolRegistry:
    """Registry for managing tools available to the agent."""
    
    def __init__(self):
        """Initialize the tool registry."""
        self.tools: Dict[str, Tool] = {}
        logger.info("ToolRegistry initialized")
    
    def register_tool(
        self,
        name: str,
        description: str,
        func: Callable,
        parameters: Dict[str, Any] = None
    ) -> Tool:
        """Register a new tool.
        
        Args:
            name: Tool name
            description: Tool description
            func: Async function implementing the tool
            parameters: Tool parameter schema
        
        Returns:
            Registered Tool object
        
        Example:
            >>> registry = ToolRegistry()
            >>> async def search_web(query: str) -> str:
            ...     return f"Search results for {query}"
            >>> registry.register_tool(
            ...     name="search",
            ...     description="Search the web",
            ...     func=search_web,
            ...     parameters={"query": {"type": "string"}}
            ... )
        """
        tool = Tool(name, description, func, parameters)
        self.tools[name] = tool
        logger.info(f"Tool registered: {name}")
        return tool
    
    def get_tool(self, name: str) -> Tool:
        """Get a registered tool by name.
        
        Args:
            name: Tool name
        
        Returns:
            Tool object or None if not found
        """
        return self.tools.get(name)
    
    def get_all_tools(self) -> List[str]:
        """Get names of all registered tools.
        
        Returns:
            List of tool names
        """
        return list(self.tools.keys())
    
    def get_tools_schema(self) -> List[Dict[str, Any]]:
        """Get JSON schemas for all tools.
        
        Returns:
            List of tool schemas
        """
        return [tool.to_schema() for tool in self.tools.values()]
    
    async def execute_tool(self, tool_name: str, **kwargs) -> Any:
        """Execute a registered tool.
        
        Args:
            tool_name: Name of the tool to execute
            **kwargs: Tool parameters
        
        Returns:
            Tool execution result
        
        Raises:
            ValueError: If tool not found
        """
        tool = self.get_tool(tool_name)
        if not tool:
            raise ValueError(f"Tool '{tool_name}' not found")
        
        logger.debug(f"Executing tool: {tool_name}")
        result = await tool.execute(**kwargs)
        logger.debug(f"Tool execution complete: {tool_name}")
        return result
    
    def unregister_tool(self, name: str) -> bool:
        """Unregister a tool.
        
        Args:
            name: Tool name
        
        Returns:
            True if tool was unregistered, False if not found
        """
        if name in self.tools:
            del self.tools[name]
            logger.info(f"Tool unregistered: {name}")
            return True
        return False


# Example: Adding a simple tool
# Uncomment and modify as needed when adding your first tool

# async def example_tool(query: str) -> str:
#     """Example tool function.
#     
#     Args:
#         query: Example query parameter
#     
#     Returns:
#         Example result
#     """
#     return f"Example tool executed with query: {query}"

# Example of how to register it:
# registry = ToolRegistry()
# registry.register_tool(
#     name="example",
#     description="An example tool",
#     func=example_tool,
#     parameters={"query": {"type": "string"}}
# )