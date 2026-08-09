# Financial Risk & Forensic Accounting Screener

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A financial risk screening tool designed for analyzing earnings quality, working capital efficiency, and identifying potential risk signals in financial disclosures.

## Core Features

| Feature | Description |
| :--- | :--- |
| **Earnings Quality Analysis** | Analyzes discrepancies between Net Income and Operating Cash Flow (CFO). |
| **Text Analysis** | Scans disclosures for risk signals like auditor changes or going concern issues. |
| **Working Capital Analysis** | Monitors inventory management and receivables trends. |
| **Reporting** | Generates structured HTML summaries for financial analysis. |

## Technical Architecture

### 1. Text Analysis Engine (`src/nlp/`)
Detects qualitative risk signals in financial reports using pattern matching and context analysis.

### 2. Scoring Engine (`src/scoring/`)
Calculates a **Risk Score (0-100)** based on:
*   **Accrual Ratio**: Analyzing non-cash earnings components.
*   **Inventory/Revenue Trends**: Monitoring divergence between stock levels and sales.
*   **Disclosure Risk**: Weighting of detected risk signals.

### 3. Reporting Pipeline (`src/reporting/`)
Converts analysis results into a structured **HTML Risk Report** with severity levels and summaries.

## Project Structure

```text
/financial-risk-screener
├── README.md               # Project documentation
├── LIMITATIONS.md          # Disclosure of system boundaries
├── requirements.txt        # Python dependencies
├── main.py                 # Main execution script
├── setup_demo_data.py      # Utility to initialize demo environment
├── src/
    ├── ingestion/          # Data loading and normalization
    ├── nlp/                # Risk detection logic
    ├── scoring/            # Risk scoring engine
    ├── reporting/          # HTML report generation
    ├── models.py           # Financial data structures
    └── pipeline.py         # Execution logic
```

## Getting Started

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/gilhermanns/financial-risk-screener.git
   cd financial-risk-screener
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## License & Disclaimer

This project is licensed under the MIT License. It is designed as a screening tool and should not replace professional audit or due diligence procedures.

---

*Entwickelt mit Unterstützung von Claude Code (Anthropic).*
