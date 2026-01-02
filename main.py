from src.models import FinancialData, Metric
from src.ingestion.loader import ConfigLoader
from src.pipeline import RiskScreeningPipeline
from src.reporting.html_gen import HTMLReporter

def main():
    print("--- PE Financial Risk Screener ---")
    
    # 1. Load Config
    config = ConfigLoader.load_sector_config("data/sector_config.yaml")
    
    # 2. Mock Data
    companies = [
        FinancialData(
            company_id="SafeCo",
            time_series={
                Metric.NET_INCOME: {2022: 100, 2023: 110},
                Metric.CFO: {2022: 120, 2023: 130},
                Metric.REVENUE: {2022: 1000, 2023: 1100},
                Metric.INVENTORY: {2022: 200, 2023: 210}
            }
        ),
        FinancialData(
            company_id="RiskCo",
            time_series={
                Metric.NET_INCOME: {2022: 100, 2023: 150},
                Metric.CFO: {2022: 20, 2023: 10},
                Metric.REVENUE: {2022: 1000, 2023: 1100},
                Metric.INVENTORY: {2022: 200, 2023: 500}
            }
        )
    ]
    
    notes = {
        "SafeCo": "The company maintains strong internal controls. No material weaknesses identified.",
        "RiskCo": "The auditor resigned following a disagreement over revenue recognition. There is significant going concern uncertainty."
    }
    
    # 3. Run Pipeline
    pipeline = RiskScreeningPipeline(config)
    results = pipeline.run(companies, notes)
    
    # 4. Report
    HTMLReporter.generate(results, "output/portfolio_summary.html")
    print("[+] Screening complete. Report generated: output/portfolio_summary.html")

if __name__ == "__main__":
    main()
