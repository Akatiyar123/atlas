from pathlib import Path

import pytest

from atlas.core.issues import ValidationIssue
from atlas.core.result import MetricResult
from atlas.report import EvaluationReport, registry
from atlas.report.reporters import CsvReporter, HtmlReporter, JsonReporter, MarkdownReporter


@pytest.fixture
def report() -> EvaluationReport:
    return EvaluationReport(
        dataset_name="sample.json",
        results=[
            MetricResult(
                metric="Completeness",
                score=0.95,
                passed=False,
                issues=[ValidationIssue(record=1, field="response", reason="missing")],
                metadata={"required_fields": ["response"]},
            )
        ],
    )


def test_report_serializes_all_evaluation_data(report: EvaluationReport) -> None:
    assert report.to_dict() == {
        "dataset_name": "sample.json",
        "results": [
            {
                "metric": "Completeness",
                "score": 0.95,
                "passed": False,
                "issues": [
                    {"record": 1, "field": "response", "reason": "missing"}
                ],
                "metadata": {"required_fields": ["response"]},
            }
        ],
        "overall_score": 0.95,
        "passed": False,
    }


@pytest.mark.parametrize(
    ("reporter", "filename", "expected_content"),
    [
        (JsonReporter(), "report.json", '"overall_score": 0.95'),
        (MarkdownReporter(), "report.md", "| Completeness | 0.95 | ❌ |"),
        (HtmlReporter(), "report.html", "<td>Completeness</td>"),
        (CsvReporter(), "report.csv", "Completeness,0.95,False"),
    ],
)
def test_file_reporters_write_report(
    report: EvaluationReport,
    reporter,
    filename: str,
    expected_content: str,
    tmp_path: Path,
) -> None:
    output = tmp_path / filename

    reporter.render(report, output)

    assert expected_content in output.read_text(encoding="utf-8")


def test_file_reporters_accept_string_output_paths(
    report: EvaluationReport,
    tmp_path: Path,
) -> None:
    output = tmp_path / "report.md"

    MarkdownReporter().render(report, str(output))

    assert output.exists()


def test_builtin_reporters_are_registered() -> None:
    assert registry.list() == ["console", "csv", "html", "json", "markdown"]
