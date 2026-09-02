"""Start command and initial user routing."""

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.localization import normalize_language

router = Router(name="start")


@router.message(CommandStart())
async def start(message: Message) -> None:
    language = normalize_language(message.from_user.language_code if message.from_user else None)
    await message.answer(f"Welcome to WhiteStones! Language: {language}")
