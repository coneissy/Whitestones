# Render deployment

WhiteStones runs as a Render Background Worker because the Telegram application uses long polling and needs a continuously running process.

## Deploy

1. Connect the `coneissy/Whitestones` repository to Render.
2. Create a new Blueprint and select the repository's `render.yaml`.
3. Keep the Blueprint on the `main` branch after this deployment PR is merged.
4. Set the private environment variable `TELEGRAM_BOT_TOKEN` in Render. The Blueprint intentionally uses `sync: false` so the token is never stored in Git.
5. Deploy the Blueprint.

The worker starts with `python -m app.main` and installs the package from `pyproject.toml`.

## Required secret

- `TELEGRAM_BOT_TOKEN` — the current token for the WhiteStones Telegram bot.

Do not commit this value to GitHub or place it in chat messages.
