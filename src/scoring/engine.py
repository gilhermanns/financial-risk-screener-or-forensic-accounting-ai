from ..models import FinancialData, Metric, ScoringResult

class PEScoringEngine:
    """
    PE-grade scoring engine focusing on Earnings Quality and Working Capital.
    """
    def __init__(self, config: dict):
        self.config = config.get("sectors", {}).get("default", {})
        self.weights = self.config.get("weights", {
            "earnings_quality": 0.5,
            "working_capital": 0.2,
            "nlp": 0.3
        })

    def compute_score(self, data: FinancialData, nlp_score: float, flags: list) -> ScoringResult:
        # 1. Earnings Quality (Net Income vs CFO)
        eq_score = self._calculate_earnings_quality(data)
        
        # 2. Working Capital Efficiency
        wc_score = self._calculate_wc_efficiency(data)
        
        # 3. Final Weighted Score
        final_score = (
            eq_score * self.weights["earnings_quality"] +
            wc_score * self.weights["working_capital"] +
            nlp_score * self.weights["nlp"]
        )
        
        category = "Low Risk"
        if final_score > 70: category = "High Risk"
        elif final_score > 40: category = "Medium Risk"
        
        return ScoringResult(
            company_id=data.company_id,
            final_score=round(final_score, 1),
            risk_category=category,
            breakdown={
                "earnings_quality": round(eq_score, 1),
                "working_capital": round(wc_score, 1),
                "nlp": round(nlp_score, 1)
            },
            flags=flags
        )

    def _calculate_earnings_quality(self, data: FinancialData) -> float:
        # Simplified: If CFO < Net Income, risk increases
        ni = sum(data.time_series.get(Metric.NET_INCOME, {}).values())
        cfo = sum(data.time_series.get(Metric.CFO, {}).values())
        if ni <= 0: return 0
        ratio = cfo / ni
        if ratio >= 1.0: return 20
        if ratio >= 0.7: return 50
        return 100

    def _calculate_wc_efficiency(self, data: FinancialData) -> float:
        # Simplified: If Inventory growth > Revenue growth, risk increases
        revs = list(data.time_series.get(Metric.REVENUE, {}).values())
        invs = list(data.time_series.get(Metric.INVENTORY, {}).values())
        if len(revs) < 2: return 30
        
        rev_growth = (revs[-1] / revs[0]) - 1
        inv_growth = (invs[-1] / invs[0]) - 1
        
        if inv_growth > rev_growth + 0.1: return 80
        return 20
