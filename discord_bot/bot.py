"""Discord bot client setup and initialization."""

import os
import discord
from discord.ext import commands
from utils.logger import setup_logger
from agent.agent import DiscordAgent
from agent.config import AgentConfig

logger = setup_logger(__name__)


class MorrellBot(commands.Cog):
    """Main Discord bot cog for Morrell agent."""
    
    def __init__(self, bot: commands.Bot, agent: DiscordAgent):
        """Initialize the bot cog.
        
        Args:
            bot: Discord bot instance
            agent: Configured DiscordAgent instance
        """
        self.bot = bot
        self.agent = agent
        logger.info("MorrellBot cog initialized")
    
    @commands.Cog.listener()
    async def on_ready(self):
        """Called when the bot is ready and connected."""
        logger.info(f"Bot logged in as {self.bot.user}")
    
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        """Handle incoming messages.
        
        Args:
            message: Discord message object
        """
        # Ignore messages from the bot itself
        if message.author == self.bot.user:
            return
        
        # Ignore messages from other bots
        if message.author.bot:
            return
        
        # Process messages starting with the prefix
        prefix = os.getenv('DISCORD_PREFIX', '!')
        if message.content.startswith(prefix):
            # Remove prefix and process
            user_message = message.content[len(prefix):].strip()
            
            logger.info(f"Message from {message.author}: {user_message}")
            
            # Show typing indicator
            async with message.channel.typing():
                # Process through agent
                response = await self.agent.process_message(
                    message=user_message,
                    user_id=str(message.author.id)
                )
                
                # Send response back to Discord
                # Split long messages if necessary (Discord has 2000 char limit)
                if len(response) > 2000:
                    for chunk in [response[i:i+2000] for i in range(0, len(response), 2000)]:
                        await message.reply(chunk)
                else:
                    await message.reply(response)


async def setup_bot() -> commands.Bot:
    """Set up and configure the Discord bot.
    
    Returns:
        Configured Discord bot instance
    """
    # Create bot instance
    intents = discord.Intents.default()
    intents.message_content = True  # Required to read message content
    
    bot = commands.Bot(
        command_prefix=os.getenv('DISCORD_PREFIX', '!'),
        intents=intents
    )
    
    # Initialize agent
    config = AgentConfig.from_env()
    agent = DiscordAgent(config)
    await agent.initialize()
    
    # Add bot cog
    await bot.add_cog(MorrellBot(bot, agent))
    
    logger.info("Discord bot setup complete")
    return bot