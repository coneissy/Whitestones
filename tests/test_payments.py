from app.bot.handlers.payments import SERVICE_PAYLOAD, SERVICE_TITLE, stars_price
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
