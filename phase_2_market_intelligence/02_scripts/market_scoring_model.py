import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
input_path = BASE_DIR / "03_output" / "clean_shopee_products.csv"
output_path = BASE_DIR / "03_output" / "market_scoring_report.txt"

df = pd.read_csv(input_path)

# =============================
# BASIC METRICS
# =============================

total_products = len(df)

# PRICE SEGMENTATION
bins = [0, 20000, 50000, 100000, 200000, 1000000]
labels = ["<20K", "20-50K", "50-100K", "100-200K", "200K+"]

df["price_range"] = pd.cut(df["price"], bins=bins, labels=labels)
price_dist = df["price_range"].value_counts().sort_index()

dominant_range = price_dist.idxmax()
dominant_count = price_dist.max()

# =============================
# SCORING
# =============================

# Competition score
competition_score = min((total_products / 200) * 100, 100)

# Saturation score
dominant_ratio = dominant_count / total_products
price_saturation_score = dominant_ratio * 100

# Gap detection
low_comp = price_dist[price_dist < price_dist.mean()]
gap_zone_factor = min(len(low_comp) * 10, 100)

# Opportunity score
opportunity_score = (
    (100 - competition_score) * 0.4 +
    (100 - price_saturation_score) * 0.4 +
    gap_zone_factor * 0.2
)

# Market attractiveness index
market_index = opportunity_score - (competition_score * 0.3)

# =============================
# SAVE REPORT
# =============================

report = f"""
=============================
MARKET SCORING MODEL REPORT
=============================

Total Products: {total_products}

Competition Score: {competition_score:.2f} / 100
Price Saturation Score: {price_saturation_score:.2f} / 100
Opportunity Score: {opportunity_score:.2f} / 100
Market Attractiveness Index: {market_index:.2f}

Dominant Price Range: {dominant_range}
Gap Zones: {", ".join(low_comp.index)}

=============================
INTERPRETATION
=============================

0–30   : Very weak opportunity
30–60  : Moderate opportunity
60–80  : Strong opportunity
80–100 : High potential market

=============================
"""

with open(output_path, "w", encoding="utf-8") as f:
    f.write(report)
