"""Opportunity matching service boundary.

The initial implementation is intentionally provider-agnostic so data sources can
be added without coupling Telegram handlers to external APIs.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Opportunity:
    title: str
    country: str
    url: str | None = None


def filter_by_country(opportunities: list[Opportunity], country: str) -> list[Opportunity]:
    normalized = country.upper()
    return [item for item in opportunities if item.country.upper() == normalized]
