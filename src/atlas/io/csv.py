import csv
from pathlib import Path

from atlas.core.dataset import Dataset


class CsvDatasetLoader:
    """Load datasets from CSV files."""

    @staticmethod
    def load(path: str | Path) -> Dataset:
        path = Path(path)

        with path.open("r", encoding="utf-8", newline="") as file:
            records = list(csv.DictReader(file))

        return Dataset(
            path=path,
            records=records,
        )
