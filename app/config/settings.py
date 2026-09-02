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
    premium_report_stars: int = 500

    @classmethod
    def from_env(cls) -> "Settings":
        try:
            premium_report_stars = int(os.getenv("PREMIUM_REPORT_STARS", "500"))
        except ValueError as exc:
            raise RuntimeError("PREMIUM_REPORT_STARS must be an integer") from exc
        if premium_report_stars <= 0:
            raise RuntimeError("PREMIUM_REPORT_STARS must be greater than zero")

        return cls(
            environment=os.getenv("WHITESTONES_ENV", "development"),
            telegram_token=os.getenv("TELEGRAM_BOT_TOKEN"),
            database_url=os.getenv("DATABASE_URL", "sqlite:///whitestones.db"),
            hubspot_enabled=os.getenv("HUBSPOT_ENABLED", "false").lower() == "true",
            default_language=os.getenv("DEFAULT_LANGUAGE", "en"),
            default_country=os.getenv("DEFAULT_COUNTRY", "LB"),
            premium_report_stars=premium_report_stars,
        )
