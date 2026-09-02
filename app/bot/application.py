"""Telegram application factory."""

from aiogram import Bot, Dispatcher

from app.config.settings import Settings


def create_dispatcher() -> Dispatcher:
    """Create a dispatcher with handlers registered by the application layer."""
    return Dispatcher()


def create_bot(settings: Settings) -> Bot:
    if not settings.telegram_token:
        raise RuntimeError("TELEGRAM_BOT_TOKEN is required to start the bot")
    return Bot(token=settings.telegram_token)
