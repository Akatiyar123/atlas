# ATLAS

**Automated Toolkit for Language Data Assessment and Scoring.**

ATLAS evaluates datasets of language-model inputs and outputs. It currently
includes a completeness metric that checks required fields are present and
non-empty, along with command-line and Python APIs for loading data and
rendering evaluation reports.

## Requirements

- Python 3.10 or later

## Installation

Install ATLAS from a checkout:

```bash
python -m pip install -e .
```

For development tools:

```bash
python -m pip install -e '.[dev]'
```

To read Excel or Parquet datasets, install the optional format dependencies:

```bash
python -m pip install -e '.[formats]'
```

## Quick start

Create a JSON dataset such as `dataset.json`:

```json
[
  {
    "id": "1",
    "prompt": "Summarize the document.",
    "response": "A short summary."
  },
  {
    "id": "2",
    "prompt": "Translate this sentence.",
    "response": ""
  }
]
```

Evaluate it from the command line:

```bash
atlas evaluate dataset.json
```

The default evaluation runs the **Completeness** metric with `id`, `prompt`,
and `response` as required fields. A score of `1.00` means every required field
in every record is present and non-empty.

## Command-line usage

```text
atlas evaluate DATASET [--format FORMAT]... [--output PATH]
atlas metrics [list]
atlas version
```

List the metrics available in the installed version:

```bash
atlas metrics list
```

### Reports

The `evaluate` command prints a terminal report by default. Use `--format` (or
`-f`) to choose a report format:

```bash
# Write a Markdown report
atlas evaluate dataset.json --format markdown --output reports/evaluation.md

# Write JSON, CSV, or HTML reports
atlas evaluate dataset.json --format json --output reports/evaluation.json
atlas evaluate dataset.json --format csv --output reports/evaluation.csv
atlas evaluate dataset.json --format html --output reports/evaluation.html
```

Supported formats are `console`, `json`, `csv`, `markdown`, and `html`. Repeat
`--format` to render more than one report; when doing so, omit `--output` and
ATLAS writes file reports as `report.json`, `report.csv`, `report.md`, or
`report.html` in the current directory.

JSON reports preserve the full evaluation result, including validation issues
and metric metadata. CSV, Markdown, and HTML reports summarize the metric,
score, and pass/fail status.

## Supported datasets

Each dataset must represent records as dictionaries/objects. ATLAS selects a
loader from the file extension:

| Format | Extensions | Notes |
| --- | --- | --- |
| JSON | `.json` | A JSON array of record objects |
| JSON Lines | `.jsonl`, `.ndjson` | One JSON object per non-empty line |
| CSV | `.csv` | Header row becomes field names |
| Excel | `.xlsx`, `.xls` | Requires `atlas[formats]` |
| Parquet | `.parquet` | Requires `atlas[formats]` |

For the built-in completeness check, a field is considered invalid when it is
missing, `null`, or an empty/whitespace-only string. Record positions in report
issues are zero-based.

## Python API

Use `Atlas` to load, evaluate, and render a report in one call:

```python
from atlas import Atlas
from atlas.core.config import MetricConfig

report = Atlas().evaluate(
    dataset_path="dataset.json",
    metrics=["completeness"],
    configs={
        "completeness": MetricConfig(
            options={"required_fields": ["id", "prompt", "response"]}
        )
    },
    formats=["json"],
    output="reports/evaluation.json",
)

print(report.overall_score)
print(report.passed)
```

To render an existing report without evaluating again, call `Atlas().render()`.
`EvaluationReport.to_dict()` returns a serializable representation containing
the dataset name, metric results, issues, metadata, overall score, and pass
status.

## Adding a metric

Metrics subclass `atlas.core.Metric` and are registered with the `@metric`
decorator. Implement `evaluate()` to return a `MetricResult`; optional
`setup()` and `teardown()` hooks receive the dataset and configuration through
the evaluation context. Ensure the module defining a metric is imported before
the metric is requested.

```python
from atlas.core import Metric, MetricResult
from atlas.decorators import metric


@metric
class RecordCount(Metric):
    id = "DQ002"
    name = "Record Count"
    description = "Counts dataset records."
    category = "Data Quality"

    def evaluate(self, context):
        count = len(context.dataset.records)
        return MetricResult(
            metric=self.name,
            score=1.0,
            passed=True,
            metadata={"record_count": count},
        )
```

## Development

Run the test suite with:

```bash
python -m pytest
```