from app.config.settings import Settings
from app.localization import normalize_language
from app.services.opportunities import Opportunity, filter_by_country
from app.services.referrals import create_referral_code


def test_settings_defaults_are_safe() -> None:
    settings = Settings()
    assert settings.environment == "development"
    assert settings.telegram_token is None


def test_language_normalization() -> None:
    assert normalize_language("en-US") == "en"
    assert normalize_language("ar") == "ar"
    assert normalize_language("xx") == "en"


def test_country_filtering() -> None:
    items = [Opportunity("A", "LB"), Opportunity("B", "AF")]
    assert filter_by_country(items, "lb")[0].title == "A"


def test_referral_codes_are_prefixed_and_nonempty() -> None:
    code = create_referral_code(123)
    assert code.startswith("ws7b")
    assert len(code) > 6
