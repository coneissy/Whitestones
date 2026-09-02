"""Typed environment-backed settings."""

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    environment: str = "development"
    telegram_token: str | None = None
    database_url: str = "sqlite:///whitestones.db"
    hubspot_enabled: bool = False
    default_language: str = "en"
    default_country: str = "LB"

    @classmethod
    def from_env(cls) -> "Settings":
        return cls(
            environment=os.getenv("WHITESTONES_ENV", "development"),
            telegram_token=os.getenv("TELEGRAM_BOT_TOKEN"),
            database_url=os.getenv("DATABASE_URL", "sqlite:///whitestones.db"),
            hubspot_enabled=os.getenv("HUBSPOT_ENABLED", "false").lower() == "true",
            default_language=os.getenv("DEFAULT_LANGUAGE", "en"),
            default_country=os.getenv("DEFAULT_COUNTRY", "LB"),
        )
