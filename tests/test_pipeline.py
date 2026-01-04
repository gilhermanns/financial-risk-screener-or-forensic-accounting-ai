from src.models import FinancialData, Metric
from src.scoring.engine import PEScoringEngine

def test_score_bounds():
    config = {
        "sectors": {
            "default": {
                "weights": {
                    "earnings_quality": 0.5,
                    "working_capital": 0.2,
                    "nlp": 0.3
                }
            }
        }
    }

    fin = FinancialData(
        company_id="TestCo",
        time_series={
            Metric.NET_INCOME: {2023: 100},
            Metric.CFO: {2023: 10},
            Metric.REVENUE: {2023: 100},
            Metric.INVENTORY: {2023: 200}
        }
    )

    engine = PEScoringEngine(config)
    result = engine.compute_score(fin, 100, ["Test Flag"])

    assert 0 <= result.final_score <= 100
