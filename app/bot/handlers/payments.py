"""Telegram Stars payment handlers for digital services."""

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import LabeledPrice, Message, PreCheckoutQuery

from app.config.settings import Settings

router = Router(name="payments")

SERVICE_TITLE = "WhiteStones Premium Opportunity Report"
SERVICE_DESCRIPTION = "One premium WhiteStones opportunity report delivered in Telegram."
SERVICE_PAYLOAD = "whitestones:premium-opportunity-report:v1"


def stars_price() -> int:
    """Return the configured price in Telegram Stars."""
    return Settings.from_env().premium_report_stars


@router.message(Command("buy"))
async def buy(message: Message) -> None:
    """Send a Telegram Stars invoice for the first paid WhiteStones service."""
    await message.answer_invoice(
        title=SERVICE_TITLE,
        description=SERVICE_DESCRIPTION,
        payload=SERVICE_PAYLOAD,
        provider_token="",
        currency="XTR",
        prices=[LabeledPrice(label=SERVICE_TITLE, amount=stars_price())],
    )


@router.pre_checkout_query()
async def pre_checkout(query: PreCheckoutQuery) -> None:
    """Approve a valid WhiteStones Stars checkout."""
    if query.invoice_payload != SERVICE_PAYLOAD:
        await query.answer(ok=False, error_message="This WhiteStones order is no longer valid.")
        return
    await query.answer(ok=True)


@router.message(lambda message: message.successful_payment is not None)
async def successful_payment(message: Message) -> None:
    """Acknowledge a completed Stars payment and deliver the purchased service."""
    payment = message.successful_payment
    if payment is None or payment.invoice_payload != SERVICE_PAYLOAD:
        return

    await message.answer(
        "⭐ Payment received! Your WhiteStones Premium Opportunity Report is being prepared.\n"
        "You will receive it here shortly."
    )
