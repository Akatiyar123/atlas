from pathlib import Path

import pytest

from atlas.io import DatasetLoader


pd = pytest.importorskip("pandas")


@pytest.mark.parametrize(
    ("filename", "writer"),
    [
        ("sample.xlsx", lambda frame, path: frame.to_excel(path, index=False)),
        ("sample.parquet", lambda frame, path: frame.to_parquet(path, index=False)),
    ],
)
def test_optional_tabular_loaders(
    tmp_path: Path,
    filename: str,
    writer,
) -> None:
    path = tmp_path / filename
    writer(pd.DataFrame([{"id": 1, "prompt": "Hello"}]), path)

    assert DatasetLoader.load(path).records == [{"id": 1, "prompt": "Hello"}]
