"""Core agent logic using GitHub Copilot Agent with Microsoft Agent Framework."""

import asyncio
from utils.logger import setup_logger
from agent.config import AgentConfig
from tools.tool_registry import ToolRegistry

logger = setup_logger(__name__)


class DiscordAgent:
    """Discord Agent using GitHub Copilot Agent with Microsoft Agent Framework.

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
        """Initialize the GitHub Copilot Agent via Microsoft Agent Framework."""
        logger.info("Setting up GitHub Copilot Agent (Microsoft Agent Framework)...")

        try:
            from agent_framework.github import GitHubCopilotAgent

            if not self.config.github_token:
                raise ValueError(
                    "GITHUB_TOKEN is not set. "
                    "Please add your GitHub personal access token to the .env file."
                )

            self.agent = GitHubCopilotAgent(
                default_options={
                    "instructions": self.config.system_prompt,
                    "model": self.config.model,
                    "temperature": self.config.temperature,
                    "max_tokens": self.config.max_tokens,
                    "api_endpoint": self.config.api_endpoint,
                    "token": self.config.github_token,
                }
            )

            self._register_tools()
            logger.info(f"{self.config.name} agent initialized successfully")

        except ImportError:
            logger.error(
                "agent-framework-github-copilot is not installed. "
                "Run: pip install copilot-sdk agent-framework-github-copilot"
            )
            raise

    def _register_tools(self):
        """Register available tools with the agent."""
        tools = self.tool_registry.get_all_tools()

        if tools:
            logger.info(f"Registering {len(tools)} tool(s) with agent...")
            for tool_name in tools:
                logger.debug(f"Registered tool: {tool_name}")
        else:
            logger.info("No tools registered yet")

    async def process_message(self, message: str, user_id: str = None) -> str:
        """Process a message through the GitHub Copilot Agent.

        Args:
            message: The message to process
            user_id: Optional Discord user ID for context

        Returns:
            Agent's response
        """
        logger.debug(f"Processing message from user {user_id}: {message}")

        if self.agent is None:
            logger.error("Agent is not initialized")
            return "Sorry, the agent is not ready. Please try again later."

        try:
            async with self.agent:
                result = await self.agent.run(message)

            response = str(result) if result else "I couldn't generate a response."
            logger.debug(f"Agent response: {response}")
            return response

        except Exception as e:
            logger.error(f"Error processing message: {e}", exc_info=True)
            return "Sorry, I encountered an error processing your message."

    async def shutdown(self):
        """Clean up and shutdown the agent."""
        logger.info("Shutting down agent...")
        self.agent = None
        logger.info("Agent shutdown complete")