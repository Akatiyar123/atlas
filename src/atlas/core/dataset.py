from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class Dataset:
    path: Path
    records: list[dict]
