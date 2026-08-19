# Financial Risk & Forensic Accounting Screener

[![Tests](https://github.com/gilhermanns/financial-risk-screener/actions/workflows/tests.yml/badge.svg)](https://github.com/gilhermanns/financial-risk-screener/actions/workflows/tests.yml)

A screening prototype for reviewing **earnings quality, working-capital patterns and selected disclosure-risk signals**. It turns a defined demonstration dataset and qualitative notes into an HTML review report; it is intended to support, not replace, financial due diligence.

## Review workflow

| Module | Review focus |
|---|---|
| Earnings quality | Difference between net income and operating cash flow |
| Working capital | Inventory and receivables trends relative to revenue |
| Disclosure screening | Rule-based signals such as auditor changes and going-concern language |
| Report generation | An HTML summary with score components, severity labels and review notes |

## Reproducible demonstration output

The repository includes a generated example report at [`output/portfolio_summary.html`](output/portfolio_summary.html). It is produced from the explicit demonstration companies and notes in `main.py`, including a deliberately higher-risk scenario. The output is therefore useful for reviewing the screening logic and report design, but it is **not** a finding about a real issuer.

## Run and validate

```bash
git clone https://github.com/gilhermanns/financial-risk-screener.git
cd financial-risk-screener
python -m pip install -r requirements.txt
python -m pytest -q
python main.py
```

The final command regenerates `output/portfolio_summary.html`. The GitHub Actions workflow executes the test suite, runs the pipeline and confirms that this report exists on each push and pull request.

## Project structure

```text
main.py                    # demonstration pipeline and explicit input scenarios
src/ingestion/             # configuration loading and normalization
src/nlp/                   # rule-based qualitative signal detection
src/scoring/               # risk-score components
src/reporting/             # HTML report generation
tests/                     # pipeline tests
output/                    # versioned demonstration report
LIMITATIONS.md             # documented model boundaries
```

## Limitations

- Scores depend on the available financial data, the selected rules and the context around a disclosure.
- A screening flag is a prompt for further review, not evidence of misconduct or financial misstatement.
- The tool does not replace audit work, transaction diligence or professional judgement.

---

*Entwickelt mit Unterstützung von Claude Code (Anthropic).*
*For research and educational purposes; not investment advice.*
