from pathlib import Path

import pytest

from atlas.io import DatasetLoader


def test_json_loader() -> None:
    dataset = DatasetLoader.load(Path(__file__).parent / "data" / "sample.json")

    assert len(dataset.records) == 3


@pytest.mark.parametrize(
    ("filename", "expected_records"),
    [
        ("sample.csv", [{"id": "1", "prompt": "Hello"}]),
        ("sample.jsonl", [{"id": 1, "prompt": "Hello"}]),
    ],
)
def test_supported_text_loaders(
    tmp_path: Path,
    filename: str,
    expected_records: list[dict],
) -> None:
    path = tmp_path / filename

    if path.suffix == ".csv":
        path.write_text("id,prompt\n1,Hello\n", encoding="utf-8")
    else:
        path.write_text('{"id": 1, "prompt": "Hello"}\n', encoding="utf-8")

    assert DatasetLoader.load(path).records == expected_records


def test_unsupported_format_raises_helpful_error(tmp_path: Path) -> None:
    path = tmp_path / "sample.txt"

    with pytest.raises(ValueError, match="Unsupported dataset format: .txt"):
        DatasetLoader.load(path)
