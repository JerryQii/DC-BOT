# DC-BOT

A production-quality starter Discord bot built with discord.py.

## Setup

### 1. Clone and install dependencies

```bash
git clone <repo-url>
cd DC-BOT
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# .venv\Scripts\activate    # Windows
pip install -r requirements.txt
```

### 2. Create a Discord application and bot

1. Go to https://discord.com/developers/applications and create a **New Application**
2. Navigate to the **Bot** tab on the left sidebar
3. Click **Add Bot** and confirm
4. Under **Privileged Gateway Intents**, enable **Message Content Intent** (required for reading message content)
5. Click **Reset Token** and copy the token

### 3. Configure environment

```bash
cp .env.example .env
```

Edit `.env` and paste your bot token:

```
DISCORD_BOT_TOKEN=your-bot-token-here
```

### 4. Invite the bot to your server

1. In the Discord Developer Portal, go to **OAuth2 > URL Generator**
2. Under **Scopes**, check `bot`
3. Under **Bot Permissions**, check:
   - **Send Messages**
   - **Read Message History**
4. Copy the generated URL and open it in a browser
5. Select a server and authorize

### 5. Run

```bash
python -m src.main
```

You should see the bot come online in your server. Type `hello` or `ping` in any channel — the bot will reply.

## Project Structure

```
DC-BOT/
├── .env.example          # Template for secrets
├── .gitignore
├── README.md
├── requirements.txt
└── src/
    ├── main.py           # Entrypoint
    ├── config.py         # Env loading and validation
    ├── bot.py            # Bot subclass with cog loading
    ├── logging_setup.py  # Logging configuration
    └── cogs/
        └── ping.py       # Ping/hello reply feature
```

## Adding Features

Create new cogs under `src/cogs/` and register them in the `COGS` list in `src/bot.py`:

```python
# src/cogs/my_feature.py
from discord.ext import commands

class MyFeature(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        ...
```

```python
# src/bot.py
COGS = [
    "src.cogs.ping",
    "src.cogs.my_feature",   # <-- add here
]
```
