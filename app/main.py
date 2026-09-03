"""WhiteStones application entry point."""

import asyncio
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread

from app.bot.application import create_bot, create_dispatcher
from app.bot.handlers.payments import router as payments_router
from app.bot.handlers.start import router as start_router
from app.config.settings import Settings


def healthcheck() -> dict[str, str]:
    return {"status": "ok", "service": "whitestones"}


class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:  # noqa: N802
        if self.path not in ("/", "/health", "/healthz"):
            self.send_response(404)
            self.end_headers()
            return
        body = b'{"status":"ok","service":"whitestones"}'
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format: str, *args: object) -> None:
        return


def start_health_server() -> ThreadingHTTPServer:
    port = int(os.getenv("PORT", "10000"))
    server = ThreadingHTTPServer(("0.0.0.0", port), HealthHandler)
    Thread(target=server.serve_forever, daemon=True).start()
    return server


def build_dispatcher():
    dispatcher = create_dispatcher()
    dispatcher.include_router(start_router)
    dispatcher.include_router(payments_router)
    return dispatcher


async def run() -> None:
    settings = Settings.from_env()
    server = start_health_server()
    bot = create_bot(settings)
    dispatcher = build_dispatcher()
    try:
        await dispatcher.start_polling(bot)
    finally:
        await bot.session.close()
        server.shutdown()
        server.server_close()


if __name__ == "__main__":
    asyncio.run(run())
