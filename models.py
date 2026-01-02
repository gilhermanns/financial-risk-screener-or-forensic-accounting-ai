from enum import Enum
from dataclasses import dataclass
from typing import Dict, List

class Metric(Enum):
    NET_INCOME = "net_income"
    CFO = "operating_cash_flow"
    REVENUE = "revenue"
    INVENTORY = "inventory"
    RECEIVABLES = "receivables"

@dataclass
class FinancialData:
    company_id: str
    time_series: Dict[Metric, Dict[int, float]]

@dataclass
class ScoringResult:
    company_id: str
    final_score: float
    risk_category: str
    breakdown: Dict[str, float]
    flags: List[str]
