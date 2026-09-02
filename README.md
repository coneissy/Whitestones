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
- `assets/banners/` — premium, reusable WhiteStones campaign artwork in SVG format.
- `tests/` — unit and integration coverage.

The architecture deliberately keeps Telegram handlers separate from storage and external providers so individual services can be replaced without rewriting the bot.

## Banner collection

The redesigned campaign set is intentionally consistent: dark premium background, WhiteStones cyan accent, short calls-to-action, and qualification/availability language instead of unsupported guarantees.

- `01-hero.svg` — master brand / opportunity discovery
- `02-model-opportunities.svg` — model opportunities
- `03-affiliate.svg` — affiliate program
- `04-vip.svg` — VIP membership
- `05-platforms.svg` — platform connections
- `06-payments.svg` — payouts and payment methods
- `07-whitelabel.svg` — white-label partners
- `08-markets.svg` — global markets, including Afghanistan

These are SVG source assets so the same artwork can be reused at multiple sizes without quality loss.

## Development

1. Copy `.env.example` to `.env` and fill in local values.
2. Create a Python 3.11+ virtual environment.
3. Install development dependencies with `python -m pip install -e '.[test,lint]'`.
4. Run `ruff check .`, `ruff format --check .`, and `pytest -q`.
5. Set `TELEGRAM_BOT_TOKEN` before starting the bot with `python -m app.main`.

Never commit `.env` or production credentials.

## Render deployment

`render.yaml` defines WhiteStones as a Render background worker using Telegram long polling. In Render, create a Blueprint from this repository and set the secret environment variable `TELEGRAM_BOT_TOKEN`. Do not put the bot token in GitHub, `render.yaml`, or any committed file.

The worker starts with `python -m app.main` and installs the package with `pip install -e .`.

## Configuration

Runtime configuration is supplied through environment variables. The checked-in `.env.example` contains safe placeholders only.

## CI

GitHub Actions runs linting, formatting checks, and tests across supported Python 3.11–3.13 on pushes and pull requests targeting `main`.
