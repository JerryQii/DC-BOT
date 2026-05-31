from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass(frozen=True)
class Config:
    bot_token: str

    @classmethod
    def from_env(cls) -> Config:
        load_dotenv()
        token = os.getenv("DISCORD_BOT_TOKEN")
        if not token:
            raise ValueError("DISCORD_BOT_TOKEN is not set in environment or .env file")
        return cls(bot_token=token)
