"""Localization and country routing."""

SUPPORTED_LANGUAGES = ("en", "ar", "fr", "es")


def normalize_language(value: str | None, default: str = "en") -> str:
    candidate = (value or "").split("-")[0].lower()
    return candidate if candidate in SUPPORTED_LANGUAGES else default
