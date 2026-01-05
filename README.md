# 🔍 PE-Grade Financial Risk & Forensic Accounting Screener

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Forensic-Accounting](https://img.shields.io/badge/Focus-Forensic%20Accounting-red.svg)]()

A professional-grade financial risk screening tool designed for **Private Equity (PE) Analysts** and **Forensic Accountants**. This system triages investment targets by analyzing earnings quality, working capital efficiency, and identifying "red flags" in financial disclosures using NLP.

---

## 💡 Core Value Proposition

In Private Equity, the "Quality of Earnings" (QoE) is the most critical part of due diligence. This tool automates the initial risk triage, allowing teams to:

| Feature | Benefit |
| :--- | :--- |
| **Earnings Quality Analysis** | Detects discrepancies between Net Income and Operating Cash Flow (CFO). |
| **Forensic NLP Engine** | Scans disclosures for high-risk signals like auditor resignations or going concern issues. |
| **Working Capital Triage** | Identifies inefficient inventory management or aggressive receivables booking. |
| **Analyst-First Reporting** | Generates professional HTML summaries for Investment Committee (IC) prep. |

---

## 🛠 Technical Architecture

### 1. Forensic NLP Engine (`src/nlp/`)
Detects qualitative risk signals in financial reports. It handles complex linguistic patterns and negation (e.g., "no material weakness" vs. "material weakness identified").

### 2. PE Scoring Engine (`src/scoring/`)
Calculates a proprietary **Risk Score (0-100)** based on:
*   **Accrual Ratio**: High non-cash earnings signal potential manipulation.
*   **Inventory/Revenue Delta**: Divergence between stock levels and sales growth.
*   **Disclosure Risk**: Weighting of NLP-detected red flags.

### 3. Reporting Pipeline (`src/reporting/`)
Converts raw analysis into a structured **HTML Risk Report**, featuring color-coded severity levels and executive summaries.

---

## 📊 Project Structure

```text
/financial-statement-ai
├── README.md               # Comprehensive project documentation
├── LIMITATIONS.md          # Mature disclosure of system boundaries
├── requirements.txt        # Python dependencies
├── main.py                 # Main execution script
├── setup_demo_data.py      # Utility to initialize demo environment
├── src/
│   ├── ingestion/          # Data loading and normalization
│   ├── nlp/                # Forensic NLP and risk detection
│   ├── scoring/            # Risk scoring engine
│   ├── reporting/          # HTML report generation
│   ├── models.py           # Financial data structures
│   └── pipeline.py         # End-to-end execution logic
└── tests/
    └── test_pipeline.py    # Unit tests for scoring logic
```

---

## 🚦 Getting Started

### Prerequisites
*   Python 3.8+
*   `pandas`, `jinja2`

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/gilhermanns/financial-risk-screener-or-forensic-accounting-ai.git
   cd financial-risk-screener-or-forensic-accounting-ai
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Demo
1. Initialize the demo data:
   ```bash
   python3 setup_demo_data.py
   ```
2. Run the risk screening pipeline:
   ```bash
   python3 main.py
   ```

---

## 📈 Interpretation of Risk Scores

*   **Score < 30 (Low Risk)**: Clean financials; standard due diligence recommended.
*   **Score 30-60 (Medium Risk)**: Minor discrepancies in cash flow or working capital.
*   **Score > 60 (High Risk)**: Significant red flags; forensic audit mandatory before IC submission.

---

## 🛡 License & Disclaimer

This project is licensed under the MIT License. It is designed as a screening tool and should not replace a full Quality of Earnings (QoE) report by a certified accounting firm.
