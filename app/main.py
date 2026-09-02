"""Minimal application entry point."""


def healthcheck() -> dict[str, str]:
    return {"status": "ok", "service": "whitestones"}


if __name__ == "__main__":
    print(healthcheck())
