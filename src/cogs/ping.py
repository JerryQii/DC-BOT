from __future__ import annotations

import logging

import discord
from discord.ext import commands

logger = logging.getLogger(__name__)

TRIGGERS = {"hello", "ping"}


class Ping(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message) -> None:
        if message.author.bot:
            return

        content = message.content.strip().lower()
        if content not in TRIGGERS:
            return

        logger.info(
            "Trigger from %s in #%s: %s",
            message.author,
            message.channel,
            content,
        )
        await message.reply(f"{content}!")
