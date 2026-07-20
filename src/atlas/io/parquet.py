from pathlib import Path

from atlas.core.dataset import Dataset


class ParquetDatasetLoader:
    """Load datasets from Parquet files."""

    @staticmethod
    def load(path: str | Path) -> Dataset:
        try:
            import pandas as pd
        except ImportError as error:
            raise ImportError(
                "Parquet support requires optional dependencies. "
                "Install them with `pip install atlas[formats]`."
            ) from error

        path = Path(path)
        records = pd.read_parquet(path).where(pd.notna, None).to_dict("records")

        return Dataset(
            path=path,
            records=records,
        )
