import json
from pathlib import Path

from atlas.core.dataset import Dataset


class JsonlDatasetLoader:
    """Load datasets from JSON Lines files."""

    @staticmethod
    def load(path: str | Path) -> Dataset:
        path = Path(path)

        with path.open("r", encoding="utf-8") as file:
            records = [
                json.loads(line)
                for line in file
                if line.strip()
            ]

        return Dataset(
            path=path,
            records=records,
        )
