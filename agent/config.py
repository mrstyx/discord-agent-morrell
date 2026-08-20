"""Configuration for the Microsoft Agent Framework agent."""

import os
from dataclasses import dataclass
from utils.logger import setup_logger

logger = setup_logger(__name__)


@dataclass
class AgentConfig:
    """Configuration for the Discord Agent."""
    
    name: str
    model: str
    system_prompt: str
    log_level: str
    
    @classmethod
    def from_env(cls) -> 'AgentConfig':
        """Load configuration from environment variables."""
        config = cls(
            name=os.getenv('AGENT_NAME', 'Morrell'),
            model=os.getenv('AGENT_MODEL', 'gpt-4'),
            system_prompt=os.getenv(
                'AGENT_SYSTEM_PROMPT',
                'You are a helpful Discord bot assistant. Help users with their questions and tasks.'
            ),
            log_level=os.getenv('LOG_LEVEL', 'INFO')
        )
        logger.info(f"Agent configured: {config.name} (Model: {config.model})")
        return config