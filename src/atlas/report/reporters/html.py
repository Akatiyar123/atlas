from html import escape
from pathlib import Path

from atlas.report.base import Reporter
from atlas.report.evaluation import EvaluationReport


class HtmlReporter(Reporter):
    """Write a standalone HTML report."""

    file_extension = ".html"

    def render(
        self,
        report: EvaluationReport,
        output: str | Path | None = None,
    ) -> None:
        if output is None:
            raise ValueError("HTML reports require an output path.")

        output = Path(output)
        data = report.to_dict()
        rows = "\n".join(
            "<tr>"
            f"<td>{escape(result['metric'])}</td>"
            f"<td>{result['score']:.2f}</td>"
            f"<td>{'✅' if result['passed'] else '❌'}</td>"
            "</tr>"
            for result in data["results"]
        )
        document = f"""<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\">
  <title>ATLAS Evaluation Report</title>
  <style>body {{ font-family: sans-serif; margin: 2rem; }} table {{ border-collapse: collapse; }} th, td {{ border: 1px solid #ccc; padding: .5rem; text-align: left; }} th {{ background: #f5f5f5; }}</style>
</head>
<body>
  <h1>ATLAS Evaluation Report</h1>
  <p>Dataset: <code>{escape(data['dataset_name'])}</code></p>
  <table>
    <thead><tr><th>Metric</th><th>Score</th><th>Passed</th></tr></thead>
    <tbody>{rows}</tbody>
  </table>
  <p><strong>Overall Score:</strong> {data['overall_score']:.2f}</p>
</body>
</html>
"""
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(document, encoding="utf-8")
