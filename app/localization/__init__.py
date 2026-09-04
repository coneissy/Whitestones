"""Localization and language routing for the OxShare referral bot."""

SUPPORTED_LANGUAGES = (
    "en", "ar", "fr", "es", "de", "it", "ru", "tr", "fa", "ps",
    "hi", "ur", "pt", "zh", "ja", "ko",
)

LANGUAGE_NAMES = {
    "en": "🇬🇧 English", "ar": "🇦🇪 العربية", "fr": "🇫🇷 Français",
    "es": "🇪🇸 Español", "de": "🇩🇪 Deutsch", "it": "🇮🇹 Italiano",
    "ru": "🇷🇺 Русский", "tr": "🇹🇷 Türkçe", "fa": "🇮🇷 فارسی",
    "ps": "🇦🇫 پښتو", "hi": "🇮🇳 हिन्दी", "ur": "🇵🇰 اردو",
    "pt": "🇵🇹 Português", "zh": "🇨🇳 中文", "ja": "🇯🇵 日本語",
    "ko": "🇰🇷 한국어",
}


def normalize_language(value: str | None, default: str = "en") -> str:
    candidate = (value or "").split("-")[0].lower()
    return candidate if candidate in SUPPORTED_LANGUAGES else default
