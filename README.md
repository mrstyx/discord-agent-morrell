# Discord Agent Morrell

A Python-based Discord bot powered by the **GitHub Copilot Agent** with the **Microsoft Agent Framework**. This agent handles messages in your Discord server and generates intelligent responses using GitHub Copilot.

## Features

- 🤖 GitHub Copilot Agent integration (Microsoft Agent Framework)
- 💬 Discord.py bot connection
- 🔧 Modular tool system (ready for future tools)
- ⚙️ Environment-based configuration
- 📝 Comprehensive logging
- 🛠️ Easy to extend with new tools

## Prerequisites

- Python 3.9+
- A Discord server with bot permissions
- A Discord Bot Token ([Discord Developer Portal](https://discord.com/developers/applications))
- A GitHub personal access token with Copilot access

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
   # Edit .env with your tokens and settings
   ```

5. **Run the agent**
   ```bash
   python main.py
   ```

## Authentication Setup

### Discord Bot Token

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application and add a **Bot** user
3. Enable **Message Content Intent** under *Bot → Privileged Gateway Intents*
4. Copy the token and set `DISCORD_TOKEN` in your `.env` file

### GitHub Token (Copilot SDK)

1. Go to [GitHub Settings → Tokens](https://github.com/settings/tokens)
2. Click **Generate new token (classic)**
3. Select the following scopes: `read:user`, `copilot`
4. Copy the token and set `GITHUB_TOKEN` in your `.env` file

## Configuration

Create a `.env` file based on `.env.example`:

```
# Discord
DISCORD_TOKEN=your_discord_bot_token_here
DISCORD_PREFIX=!

# Agent
AGENT_NAME=Morrell
AGENT_MODEL=gpt-4o
AGENT_TEMPERATURE=0.7
AGENT_MAX_TOKENS=4096

# GitHub Copilot SDK
GITHUB_TOKEN=your_github_personal_access_token_here
COPILOT_API_ENDPOINT=https://api.githubcopilot.com

# Logging
LOG_LEVEL=INFO
```

## Project Structure

```
discord-agent-morrell/
├── main.py                 # Entry point
├── agent/
│   ├── __init__.py
│   ├── config.py          # Agent configuration (includes Copilot settings)
│   └── agent.py           # Copilot Agent logic
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
2. Listen for messages prefixed with `!` (configurable via `DISCORD_PREFIX`)
3. Send the message to the GitHub Copilot Agent
4. Reply with the agent-generated response

### Example

```
User:   !What is the capital of France?
Morrell: The capital of France is Paris.
```

### Adding Tools

To add new tools to the agent:

1. Create a tool module in `tools/`
2. Register it in `tools/tool_registry.py`
3. Define the tool schema for the agent
4. The agent can now use the tool automatically

See `tools/tool_registry.py` for examples.

## Customising Agent Behaviour

Edit `AGENT_SYSTEM_PROMPT` in your `.env` file to change how the agent introduces itself and behaves:

```
AGENT_SYSTEM_PROMPT=You are a snarky but helpful Discord bot. Keep answers short and witty.
```

You can also adjust `AGENT_MODEL`, `AGENT_TEMPERATURE`, and `AGENT_MAX_TOKENS` to control the model and response style.

## Architecture

### Agent Layer
- **agent/config.py**: Loads all configuration including Copilot credentials
- **agent/agent.py**: Initialises `GitHubCopilotAgent` and processes messages

### Discord Layer
- **discord_bot/bot.py**: Discord.py bot client setup
- **discord_bot/handlers.py**: Discord event handlers

### Tools Layer
- **tools/tool_registry.py**: Central registry for agent tools

## Logging

Logging is configured via `utils/logger.py` and controlled by the `LOG_LEVEL` environment variable.

## Contributing

Feel free to extend this agent with new tools and features!

## License

MIT License

## Support

For issues or questions, please open an issue on GitHub.