# WhiteStones

WhiteStones bot application foundation.

## Development

1. Copy `.env.example` to `.env` and fill in local values.
2. Create a Python 3.11+ virtual environment.
3. Install development dependencies with `python -m pip install -e '.[test,lint]'`.
4. Run `ruff check .` and `pytest -q`.

## CI

GitHub Actions runs linting and tests on pushes and pull requests targeting `main`.
