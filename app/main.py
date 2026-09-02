"""WhiteStones application entry point."""

import asyncio

from app.bot.application import create_bot, create_dispatcher
from app.bot.handlers.payments import router as payments_router
from app.bot.handlers.start import router as start_router
from app.config.settings import Settings


def healthcheck() -> dict[str, str]:
    return {"status": "ok", "service": "whitestones"}


def build_dispatcher():
    dispatcher = create_dispatcher()
    dispatcher.include_router(start_router)
    dispatcher.include_router(payments_router)
    return dispatcher


async def run() -> None:
    settings = Settings.from_env()
    bot = create_bot(settings)
    dispatcher = build_dispatcher()
    try:
        await dispatcher.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(run())
