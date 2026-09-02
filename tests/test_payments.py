from unittest.mock import Mock

from app.bot.handlers.payments import (
    SERVICE_PAYLOAD,
    SERVICE_TITLE,
    build_premium_report,
    stars_price,
)
from app.config.settings import Settings


def test_stars_payment_defaults(monkeypatch):
    monkeypatch.delenv("PREMIUM_REPORT_STARS", raising=False)
    assert Settings.from_env().premium_report_stars == 500
    assert stars_price() == 500


def test_stars_payment_contract(monkeypatch):
    monkeypatch.setenv("PREMIUM_REPORT_STARS", "250")
    assert Settings.from_env().premium_report_stars == 250
    assert SERVICE_PAYLOAD.startswith("whitestones:")
    assert SERVICE_TITLE


def test_premium_report_is_deliverable(monkeypatch):
    monkeypatch.setenv("DEFAULT_COUNTRY", "AF")
    message = Mock()
    message.from_user.language_code = "en"
    report = build_premium_report(message)
    assert "WHITE STONES" in report
    assert "Target market: AF" in report
    assert "7-day action plan" in report
