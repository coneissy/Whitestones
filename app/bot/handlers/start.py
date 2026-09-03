"""Start and basic navigation commands."""

from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from app.localization import normalize_language

router = Router(name="start")


@router.message(CommandStart())
async def start(message: Message) -> None:
    language = normalize_language(message.from_user.language_code if message.from_user else None)
    await message.answer(
        f"Welcome to WhiteStones! Language: {language}\n\n"
        "Use /help to see available commands."
    )


@router.message(Command("help"))
async def help_command(message: Message) -> None:
    await message.answer(
        "🤍 WhiteStones Help\n\n"
        "/start — Start WhiteStones\n"
        "/howitworks — How WhiteStones works\n"
        "/menu — Open the main menu\n"
        "/buy — Get the Premium Opportunity Report\n"
        "/paysupport — Payment support\n"
        "/help — Show this help"
    )


@router.message(Command("howitworks"))
@router.message(Command("how_it_works"))
async def how_it_works(message: Message) -> None:
    await message.answer(
        "🚀 How WhiteStones Works\n\n"
        "1. Discover — explore digital and business opportunities.\n"
        "2. Choose — select an opportunity that fits your market and skills.\n"
        "3. Start — follow a practical action plan to validate demand.\n"
        "4. Grow — improve the offer, collect feedback and build higher-value services.\n\n"
        "WhiteStones is designed for opportunity discovery, referrals, analytics and future partner integrations."
    )


@router.message(Command("menu"))
async def menu(message: Message) -> None:
    await message.answer(
        "🤍 WhiteStones Menu\n\n"
        "🔎 /howitworks — How it works\n"
        "⭐ /buy — Premium Opportunity Report\n"
        "💳 /paysupport — Payment support\n"
        "❓ /help — Help and commands"
    )
