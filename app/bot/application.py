"""Telegram application factory."""

from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.client.telegram import TelegramAPIServer

from app.config.settings import Settings


def create_dispatcher() -> Dispatcher:
    """Create a dispatcher with handlers registered by the application layer."""
    return Dispatcher()


def create_bot(settings: Settings) -> Bot:
    if not settings.telegram_token:
        raise RuntimeError("TELEGRAM_BOT_TOKEN is required to start the bot")

    # Telegram provides a completely separate Bot API test environment.
    # Keep production as the default; enable test mode only for a test bot/token.
    if settings.telegram_test_mode:
        session = AiohttpSession(api=TelegramAPIServer.TEST)
        return Bot(token=settings.telegram_token, session=session)

    return Bot(token=settings.telegram_token)
