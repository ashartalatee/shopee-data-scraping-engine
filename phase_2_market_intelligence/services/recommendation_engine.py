import json
import os
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class RecommendationEngine:

    def __init__(self, input_path="reports/market_scoring.json"):
        self.input_path = input_path

    def run(self):
        logging.info("===== RECOMMENDATION ENGINE STARTED =====")

        data = self.load_data()

        score = data.get("market_attractiveness", 0)
        competition = data.get("competition_score", 0)
        saturation = data.get("price_saturation_score", 0)
        gaps = data.get("gap_zones", [])

        market_class = self.classify_market(score)
        action = self.generate_action(score)
        strategies = self.generate_strategy(competition, saturation, gaps)
        risks = self.detect_risk(competition, saturation)

        self.save_report(score, market_class, action, strategies, risks)

        logging.info("===== RECOMMENDATION ENGINE COMPLETED =====")

    # =============================
    # CORE LOGIC
    # =============================

    def classify_market(self, score):
        if score >= 80:
            return "HIGH POTENTIAL"
        elif score >= 60:
            return "STRONG"
        elif score >= 30:
            return "MODERATE"
        else:
            return "WEAK"

    def generate_action(self, score):
        if score >= 80:
            return "ENTER AGGRESSIVELY"
        elif score >= 60:
            return "ENTER WITH STRATEGY"
        elif score >= 30:
            return "ENTER WITH CAUTION"
        else:
            return "AVOID MARKET"

    def generate_strategy(self, competition, saturation, gaps):
        strategies = []

        if competition < 30:
            strategies.append("Low competition → validate demand first")

        if saturation > 70:
            strategies.append("High saturation → strong differentiation needed")

        if gaps:
            strategies.append(f"Target price gap: {', '.join(gaps)}")

        if not strategies:
            strategies.append("Standard market entry strategy")

        return strategies

    def detect_risk(self, competition, saturation):
        risks = []

        if saturation > 80:
            risks.append("High price saturation")

        if competition < 10:
            risks.append("Market may not be validated")

        if not risks:
            risks.append("Low risk detected")

        return risks

    # =============================
    # IO HANDLING
    # =============================

    def load_data(self):
        if not os.path.exists(self.input_path):
            raise FileNotFoundError(f"{self.input_path} not found")

        with open(self.input_path, "r") as f:
            return json.load(f)

    def save_report(self, score, market_class, action, strategies, risks):
        os.makedirs("reports", exist_ok=True)

        output_path = "reports/recommendation.txt"

        with open(output_path, "w") as f:
            f.write("=============================\n")
            f.write("MARKET ACTION RECOMMENDATION\n")
            f.write("=============================\n\n")

            f.write(f"Market Attractiveness: {score:.2f} → {market_class}\n\n")

            f.write("RECOMMENDED ACTION:\n")
            f.write(f"- {action}\n\n")

            f.write("STRATEGY SUGGESTION:\n")
            for s in strategies:
                f.write(f"- {s}\n")

            f.write("\nRISK:\n")
            for r in risks:
                f.write(f"- {r}\n")

        logging.info(f"Recommendation report saved to {output_path}")