from __future__ import annotations

import logging

import discord
from discord.ext import commands

from src.config import Config

logger = logging.getLogger(__name__)

COGS: list[str] = []


class DiscordBot(commands.Bot):
    def __init__(self, config: Config) -> None:
        intents = discord.Intents.default()
        intents.message_content = True

        super().__init__(
            command_prefix="!",
            intents=intents,
        )
        self._config = config

    async def setup_hook(self) -> None:
        for ext in COGS:
            await self.load_extension(ext)
            logger.info("Loaded extension: %s", ext)

    async def on_ready(self) -> None:
        logger.info("Logged in as %s (ID: %s)", self.user, self.user.id)
