from pathlib import Path

from atlas.core.dataset import Dataset


class ExcelDatasetLoader:
    """Load datasets from Excel workbooks."""

    @staticmethod
    def load(path: str | Path) -> Dataset:
        try:
            import pandas as pd
        except ImportError as error:
            raise ImportError(
                "Excel support requires optional dependencies. "
                "Install them with `pip install atlas[formats]`."
            ) from error

        path = Path(path)
        records = pd.read_excel(path).where(pd.notna, None).to_dict("records")

        return Dataset(
            path=path,
            records=records,
        )
