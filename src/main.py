from __future__ import annotations

import asyncio

from src.config import Config
from src.bot import DiscordBot
from src.logging_setup import setup_logging


async def main() -> None:
    setup_logging()
    config = Config.from_env()
    bot = DiscordBot(config)
    await bot.start(config.bot_token)


if __name__ == "__main__":
    asyncio.run(main())
