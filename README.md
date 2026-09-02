# WhiteStones

WhiteStones is a modular Telegram bot foundation for opportunity discovery, country/language routing, referrals, analytics, affiliate flows, and CRM integrations.

## Architecture

- `app/bot/` — Telegram application, routers, and handlers.
- `app/config/` — environment-backed runtime configuration.
- `app/database/` — persistence interfaces and repository contracts.
- `app/integrations/` — external service boundaries such as HubSpot.
- `app/localization/` — language normalization and localization entry points.
- `app/models/` — domain models.
- `app/services/` — business logic for opportunities, referrals, and future monetization services.
- `tests/` — unit and integration coverage.

The architecture deliberately keeps Telegram handlers separate from storage and external providers so individual services can be replaced without rewriting the bot.

## Development

1. Copy `.env.example` to `.env` and fill in local values.
2. Create a Python 3.11+ virtual environment.
3. Install development dependencies with `python -m pip install -e '.[test,lint]'`.
4. Run `ruff check .`, `ruff format --check .`, and `pytest -q`.
5. Set `TELEGRAM_BOT_TOKEN` before starting the bot with `python -m app.main`.

Never commit `.env` or production credentials.

## Configuration

Runtime configuration is supplied through environment variables. The checked-in `.env.example` contains safe placeholders only.

## CI

GitHub Actions runs linting, formatting checks, and tests across supported Python 3.11–3.13 on pushes and pull requests targeting `main`.
