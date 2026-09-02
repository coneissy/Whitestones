"""User domain model used by bot and integrations."""

from dataclasses import dataclass


@dataclass(slots=True)
class User:
    telegram_id: int
    language: str = "en"
    country: str = "LB"
    referral_code: str | None = None
    referred_by: str | None = None
