"""HubSpot integration boundary.

Credentials and API calls will be added behind this interface so bot handlers
remain independent from CRM implementation details.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class HubSpotContact:
    external_id: str
    language: str
    country: str


class HubSpotClient:
    def __init__(self, access_token: str | None = None) -> None:
        self.access_token = access_token

    @property
    def enabled(self) -> bool:
        return bool(self.access_token)
