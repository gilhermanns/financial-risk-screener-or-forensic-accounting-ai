# AI Financial Risk Screener (PE-Grade)

A professional-grade financial risk screening and forensic accounting tool designed for Private Equity (PE) investment teams. This system automates the triage of potential investment targets by analyzing multi-year financial statements and management commentary to identify elevated accounting, cash flow, and governance risks.

---

## 🎯 Strategic Objective

In the due diligence process, time is the most valuable resource. This tool acts as a **first-pass risk filter**, allowing analysts to:
- **Prioritize Diligence**: Focus manual deep-dives on "High Risk" targets first.
- **Detect Forensic Red Flags**: Identify subtle accounting anomalies and governance issues that might be missed in a standard review.
- **Standardize Risk Assessment**: Apply a consistent, data-driven risk framework across a large portfolio of potential targets.

---

## 🔍 Core Analysis Dimensions

The system evaluates targets across three critical pillars:

### 1. Earnings Quality (EQ)
- **Cash Conversion Analysis**: Compares Net Income against Operating Cash Flow (CFO) over multiple periods.
- **Anomaly Detection**: Flags companies booking significant accounting profits without corresponding cash inflows, a classic signal of aggressive revenue recognition or capitalised expenses.

### 2. Working Capital Efficiency (WC)
- **Inventory & Receivables Tracking**: Monitors growth in working capital components relative to revenue growth.
- **Cash Trap Identification**: Flags potential "cash traps" where inventory growth materially outpaces sales, signaling potential obsolescence or aggressive growth assumptions.

### 3. Forensic NLP Risk Detection
- **Governance & Audit Signals**: Scans management commentary and notes for high-risk language such as auditor resignations, restatements, or "going concern" uncertainties.
- **Context-Aware Filtering**: Employs negation handling (e.g., "no material weaknesses identified") to minimize false positives and ensure high-signal output.

---

## 🛠 Technical Architecture

The project follows a clean, modular architecture designed for professional environments:
- **`src/models.py`**: Robust data models using Python dataclasses for financial metrics and scoring results.
- **`src/scoring/`**: A weighted scoring engine that combines quantitative financial ratios with qualitative NLP signals.
- **`src/nlp/`**: A regex-based risk detector with sophisticated negation logic.
- **`src/reporting/`**: An analyst-friendly HTML report generator that provides a visual summary of the risk landscape.

---

## 📊 Project Structure

```text
financial-statement-ai/
├── src/
│   ├── ingestion/      # Data loading logic
│   ├── nlp/            # Risk detection NLP engine
│   ├── scoring/        # PE-grade scoring engine
│   ├── reporting/      # HTML report generation
│   ├── pipeline.py     # Main processing pipeline
│   └── models.py       # Data models and metrics
├── data/
│   └── sector_config.yaml
├── output/             # Generated reports (HTML)
├── tests/              # Unit tests for core logic
├── setup_demo_data.py  # Script to generate sample data
├── main.py             # Entry point
├── requirements.txt
└── README.md
```

---

## 🚦 Quick Start

### Installation
```bash
pip install -r requirements.txt
```

### Running the Screener
1. Initialize demo data:
   ```bash
   python setup_demo_data.py
   ```
2. Run the analysis:
   ```bash
   python main.py
   ```
3. View the results:
   Open `output/portfolio_summary.html` in your browser.

---

## 📈 Interpretation of Scores

- **0–40 (Low Risk)**: Healthy cash conversion, strong working capital management, and no major governance red flags.
- **41–70 (Medium Risk)**: Operational or accounting concerns (e.g., CFO lagging Net Income) requiring follow-up diligence.
- **71–100 (High Risk)**: Significant red flags in earnings quality, governance issues, or aggressive accounting practices.

---

## 🛡 Limitations & Scope

This tool is a screening and prioritization aid. It does not replace professional financial due diligence, audits, or valuation models (DCF/LBO). For a detailed breakdown of system boundaries, please refer to [LIMITATIONS.md](LIMITATIONS.md).

---

## ⚖️ License

This project is licensed under the MIT License.
