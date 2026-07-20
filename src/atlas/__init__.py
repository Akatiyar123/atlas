# Import built-in metrics once so they register with the metric registry when
# the public package API is imported.
import atlas.metrics  # noqa: F401

from .atlas import Atlas
from .version import __version__

__all__ = [
    "Atlas",
    "__version__",
]
