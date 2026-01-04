from typing import List
from .models import FinancialData, ScoringResult
from .nlp.risk_detector import RiskDetector
from .scoring.engine import PEScoringEngine

class RiskScreeningPipeline:
    def __init__(self, config: dict):
        self.nlp = RiskDetector()
        self.engine = PEScoringEngine(config)

    def run(self, companies: List[FinancialData], notes: dict) -> List[ScoringResult]:
        results = []
        for company in companies:
            text = notes.get(company.company_id, "")
            nlp_score, flags = self.nlp.analyze_text(text)
            result = self.engine.compute_score(company, nlp_score, flags)
            results.append(result)
        return results
