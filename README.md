# Discord Agent Morrell

A Python-based Discord bot powered by the Microsoft Agent Framework. This agent can handle messages in your Discord server and respond intelligently with a modular tool system for extensibility.

## Features

- 🤖 Microsoft Agent Framework integration
- 💬 Discord.py bot connection
- 🔧 Modular tool system (ready for future tools)
- ⚙️ Environment-based configuration
- 📝 Comprehensive logging
- 🛠️ Easy to extend with new tools

## Prerequisites

- Python 3.9+
- A Discord server with bot permissions
- Microsoft Agent Framework credentials (if required)
- Discord Bot Token

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/mrstyx/discord-agent-morrell.git
   cd discord-agent-morrell
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your Discord bot token and other configurations
   ```

5. **Run the agent**
   ```bash
   python main.py
   ```

## Configuration

Create a `.env` file based on `.env.example`:

```
DISCORD_TOKEN=your_discord_bot_token_here
DISCORD_PREFIX=!
AGENT_NAME=Morrell
AGENT_MODEL=gpt-4
LOG_LEVEL=INFO
```

## Project Structure

```
discord-agent-morrell/
├── main.py                 # Entry point
├── agent/
│   ├── __init__.py
│   ├── config.py          # Agent configuration
│   └── agent.py           # Core agent logic
├── discord_bot/
│   ├── __init__.py
│   ├── bot.py             # Discord bot client
│   └── handlers.py        # Discord event handlers
├── tools/
│   ├── __init__.py
│   └── tool_registry.py   # Tool management system
├── utils/
│   ├── __init__.py
│   └── logger.py          # Logging configuration
├── requirements.txt       # Python dependencies
├── .env.example          # Environment template
└── README.md             # This file
```

## Usage

Once the bot is running, it will:
1. Connect to your Discord server
2. Listen for messages
3. Process them through the Microsoft Agent Framework
4. Respond with agent-generated responses

### Adding Tools

To add new tools to the agent:

1. Create a tool module in `tools/`
2. Register it in `tools/tool_registry.py`
3. Define the tool schema for the agent
4. The agent can now use the tool automatically

See `tools/tool_registry.py` for examples.

## Architecture

### Agent Layer
- **agent/config.py**: Configuration and initialization of the Microsoft Agent Framework agent
- **agent/agent.py**: Core agent logic and message processing

### Discord Layer
- **discord_bot/bot.py**: Discord.py bot client setup
- **discord_bot/handlers.py**: Discord event handlers (on_message, etc.)

### Tools Layer
- **tools/tool_registry.py**: Central registry for agent tools
- Each tool is independently defined and pluggable

## Logging

Logging is configured via `utils/logger.py` and controlled by the `LOG_LEVEL` environment variable.

## Contributing

Feel free to extend this agent with new tools and features!

## License

MIT License

## Support

For issues or questions, please open an issue on GitHub.