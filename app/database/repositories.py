"""Repository interfaces; concrete storage can be added without changing handlers."""

from typing import Protocol

from app.models.user import User


class UserRepository(Protocol):
    def get(self, telegram_id: int) -> User | None: ...

    def save(self, user: User) -> None: ...
