"""Core agent logic using Microsoft Agent Framework."""

import asyncio
from utils.logger import setup_logger
from agent.config import AgentConfig
from tools.tool_registry import ToolRegistry

logger = setup_logger(__name__)


class DiscordAgent:
    """Discord Agent using Microsoft Agent Framework.
    
    This class manages the agent's lifecycle, tool integration,
    and message processing.
    """
    
    def __init__(self, config: AgentConfig):
        """Initialize the Discord Agent.
        
        Args:
            config: Agent configuration
        """
        self.config = config
        self.tool_registry = ToolRegistry()
        self.agent = None
        
        logger.info(f"Initializing {config.name} agent...")
    
    async def initialize(self):
        """Initialize the Microsoft Agent Framework agent.
        
        TODO: Implement actual Microsoft Agent Framework initialization.
        This is a placeholder for the real implementation.
        """
        logger.info("Setting up Microsoft Agent Framework...")
        
        # TODO: Replace with actual Microsoft Agent Framework initialization
        # Example placeholder:
        # self.agent = await create_agent(
        #     name=self.config.name,
        #     model=self.config.model,
        #     system_prompt=self.config.system_prompt
        # )
        
        # Register available tools
        self._register_tools()
        
        logger.info(f"{self.config.name} agent initialized successfully")
    
    def _register_tools(self):
        """Register available tools with the agent."""
        # Get all registered tools
        tools = self.tool_registry.get_all_tools()
        
        if tools:
            logger.info(f"Registering {len(tools)} tool(s) with agent...")
            for tool_name in tools:
                logger.debug(f"Registered tool: {tool_name}")
        else:
            logger.info("No tools registered yet")
    
    async def process_message(self, message: str, user_id: str = None) -> str:
        """Process a message through the agent.
        
        Args:
            message: The message to process
            user_id: Optional Discord user ID for context
        
        Returns:
            Agent's response
        """
        logger.debug(f"Processing message from user {user_id}: {message}")
        
        try:
            # TODO: Implement actual message processing with Microsoft Agent Framework
            # Example placeholder:
            # response = await self.agent.process(
            #     message=message,
            #     context={'user_id': user_id}
            # )
            
            # For now, return a placeholder response
            response = f"I received your message: '{message}'. The agent is being configured."
            
            logger.debug(f"Agent response: {response}")
            return response
            
        except Exception as e:
            logger.error(f"Error processing message: {e}", exc_info=True)
            return "Sorry, I encountered an error processing your message."
    
    async def shutdown(self):
        """Clean up and shutdown the agent."""
        logger.info("Shutting down agent...")
        # TODO: Implement cleanup logic for Microsoft Agent Framework
        logger.info("Agent shutdown complete")