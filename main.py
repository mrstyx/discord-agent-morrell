"""Main entry point for Discord Agent Morrell."""

import asyncio
import os
from dotenv import load_dotenv
from utils.logger import setup_logger
from discord_bot.bot import setup_bot

# Load environment variables
load_dotenv()

logger = setup_logger(__name__)


async def main():
    """Main function to start the Discord bot."""
    try:
        logger.info("Starting Discord Agent Morrell...")
        
        # Get Discord token
        discord_token = os.getenv('DISCORD_TOKEN')
        if not discord_token:
            logger.error("DISCORD_TOKEN not found in environment variables")
            logger.error("Please set DISCORD_TOKEN in your .env file")
            return
        
        # Set up bot
        bot = await setup_bot()
        
        # Start bot
        logger.info("Connecting to Discord...")
        await bot.start(discord_token)
        
    except KeyboardInterrupt:
        logger.info("Received keyboard interrupt, shutting down...")
    except Exception as e:
        logger.error(f"Fatal error: {e}", exc_info=True)
    finally:
        logger.info("Discord Agent Morrell stopped")


if __name__ == "__main__":
    asyncio.run(main())