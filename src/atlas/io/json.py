import json
from pathlib import Path

from atlas.core.dataset import Dataset


class JsonDatasetLoader:
    """Load datasets from JSON files."""

    @staticmethod
    def load(path: str | Path) -> Dataset:
        path = Path(path)

        with path.open("r", encoding="utf-8") as file:
            records = json.load(file)

        return Dataset(
            path=path,
            records=records,
        )
