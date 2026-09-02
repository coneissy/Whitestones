"""Telegram Stars payment handlers for digital services."""

import logging

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import LabeledPrice, Message, PreCheckoutQuery

from app.config.settings import Settings

router = Router(name="payments")
logger = logging.getLogger(__name__)

SERVICE_TITLE = "WhiteStones Premium Opportunity Report"
SERVICE_DESCRIPTION = "A premium WhiteStones opportunity starter report delivered in Telegram."
SERVICE_PAYLOAD = "whitestones:premium-opportunity-report:v1"


def stars_price() -> int:
    """Return the configured price in Telegram Stars."""
    return Settings.from_env().premium_report_stars


def build_premium_report(message: Message) -> str:
    """Build the first paid report without requiring a separate AI provider."""
    user_language = (message.from_user.language_code if message.from_user else None) or "en"
    country = Settings.from_env().default_country
    return (
        "⭐ WHITE STONES — PREMIUM OPPORTUNITY REPORT\n\n"
        f"Target market: {country}\n"
        f"Language signal: {user_language}\n\n"
        "1. Digital services: offer CV, translation, business-document and social-content help.\n"
        "2. Local business support: create menus, listings, simple landing copy and customer messages.\n"
        "3. Opportunity workflow: start with one service, validate demand, collect testimonials, then add higher-value packages.\n\n"
        "🚀 7-day action plan\n"
        "Day 1: choose one service and define the offer.\n"
        "Day 2: publish three sample results.\n"
        "Day 3: contact 20 potential customers.\n"
        "Days 4–5: deliver the first jobs quickly and request feedback.\n"
        "Days 6–7: package the best-selling service and raise the price.\n\n"
        "This is your starter report. WhiteStones can expand it with live opportunity data as additional integrations are enabled."
    )


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


@router.message(Command("paysupport"))
async def pay_support(message: Message) -> None:
    """Provide the required payment-support entry point."""
    await message.answer(
        "Payment support: please send your payment receipt/charge information here "
        "and describe the issue. WhiteStones will review it."
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

    # Keep the charge identifier in structured logs for reconciliation/refunds.
    logger.info(
        "WhiteStones Stars payment received: user_id=%s charge_id=%s amount=%s",
        message.from_user.id if message.from_user else None,
        payment.telegram_payment_charge_id,
        payment.total_amount,
    )
    await message.answer(
        "⭐ Payment received! Your Premium Opportunity Report is ready:\n\n"
        + build_premium_report(message)
    )
