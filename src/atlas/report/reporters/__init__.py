from atlas.report.registry import registry

from .console import ConsoleReporter
from .csv import CsvReporter
from .html import HtmlReporter
from .json import JsonReporter
from .markdown import MarkdownReporter

registry.register("console", ConsoleReporter)
registry.register("csv", CsvReporter)
registry.register("html", HtmlReporter)
registry.register("json", JsonReporter)
registry.register("markdown", MarkdownReporter)

__all__ = [
    "ConsoleReporter",
    "CsvReporter",
    "HtmlReporter",
    "JsonReporter",
    "MarkdownReporter",
]
