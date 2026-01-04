import re
from typing import List, Tuple

class RiskDetector:
    """
    NLP engine for detecting forensic accounting and governance red flags.
    """
    RED_FLAGS = {
        "Auditor Resignation": re.compile(r"(?i)auditor\s+(?:resigned|resignation|terminated|withdrawn)"),
        "Going Concern": re.compile(r"(?i)going\s+concern\s+uncertainty"),
        "Restatement": re.compile(r"(?i)restatement\s+of\s+financial\s+statements"),
        "Material Weakness": re.compile(r"(?i)material\s+weakness\s+in\s+internal\s+control")
    }

    NEGATIONS = [
        r"no\s+material\s+weakness",
        r"not\s+a\s+going\s+concern",
        r"absence\s+of\s+restatements"
    ]

    def analyze_text(self, text: str) -> Tuple[float, List[str]]:
        found_flags = []
        for name, pattern in self.RED_FLAGS.items():
            if pattern.search(text):
                # Check for negations
                is_negated = False
                for neg in self.NEGATIONS:
                    if re.search(f"(?i){neg}", text):
                        is_negated = True
                        break
                
                if not is_negated:
                    found_flags.append(name)
        
        score = min(len(found_flags) * 40, 100)
        return float(score), found_flags
