"""Referral attribution primitives."""

import secrets


def create_referral_code(telegram_id: int) -> str:
    """Create a short non-secret referral identifier."""
    suffix = secrets.token_urlsafe(4).replace("-", "").replace("_", "")[:6]
    return f"ws{telegram_id:x}{suffix}"
