import os
from typing import List
from ..models import ScoringResult

class HTMLReporter:
    """Generates analyst-friendly HTML reports."""
    
    TEMPLATE = """
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; background: #f4f7f6; }}
            .card {{ background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin-bottom: 20px; }}
            .high-risk {{ border-left: 10px solid #e74c3c; }}
            .medium-risk {{ border-left: 10px solid #f39c12; }}
            .low-risk {{ border-left: 10px solid #2ecc71; }}
            h1 {{ color: #2c3e50; }}
            .score {{ font-size: 24px; font-weight: bold; }}
        </style>
    </head>
    <body>
        <h1>PE Portfolio Risk Summary</h1>
        {content}
    </body>
    </html>
    """

    @staticmethod
    def generate(results: List[ScoringResult], output_path: str):
        cards = []
        for r in results:
            risk_class = r.risk_category.lower().replace(" ", "-")
            flags_html = "".join([f"<li>{f}</li>" for f in r.flags])
            card = f"""
            <div class="card {risk_class}">
                <h2>{r.company_id} - {r.risk_category}</h2>
                <div class="score">Risk Score: {r.final_score}/100</div>
                <p>Breakdown: EQ: {r.breakdown['earnings_quality']}, WC: {r.breakdown['working_capital']}, NLP: {r.breakdown['nlp']}</p>
                <ul>{flags_html}</ul>
            </div>
            """
            cards.append(card)
        
        html = HTMLReporter.TEMPLATE.format(content="".join(cards))
        
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w') as f:
            f.write(html)
