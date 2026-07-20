from pathlib import Path

from atlas.core.dataset import Dataset
from atlas.io.csv import CsvDatasetLoader
from atlas.io.excel import ExcelDatasetLoader
from atlas.io.json import JsonDatasetLoader
from atlas.io.jsonl import JsonlDatasetLoader
from atlas.io.parquet import ParquetDatasetLoader


class DatasetLoader:
    """Load a dataset using the loader registered for its file extension."""

    LOADERS = {
        ".csv": CsvDatasetLoader,
        ".jsonl": JsonlDatasetLoader,
        ".ndjson": JsonlDatasetLoader,
        ".json": JsonDatasetLoader,
        ".xlsx": ExcelDatasetLoader,
        ".xls": ExcelDatasetLoader,
        ".parquet": ParquetDatasetLoader,
    }

    @classmethod
    def load(cls, path: str | Path) -> Dataset:
        path = Path(path)
        suffix = path.suffix.lower()
        loader = cls.LOADERS.get(suffix)

        if loader is None:
            raise ValueError(f"Unsupported dataset format: {suffix or '<none>'}")

        return loader.load(path)
