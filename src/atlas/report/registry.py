from __future__ import annotations

from typing import Type

from atlas.report.base import Reporter


class ReporterRegistry:
    """Registry of available report output formats."""

    def __init__(self) -> None:
        self._reporters: dict[str, Type[Reporter]] = {}

    def register(self, name: str, reporter: Type[Reporter]) -> None:
        self._reporters[name.lower()] = reporter

    def get(self, name: str) -> Type[Reporter]:
        try:
            return self._reporters[name.lower()]
        except KeyError as error:
            available = ", ".join(self.list())
            raise ValueError(
                f"Unsupported report format: {name}. Available formats: {available}"
            ) from error

    def list(self) -> list[str]:
        return sorted(self._reporters)


registry = ReporterRegistry()
