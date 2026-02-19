import pandas as pd
from pathlib import Path

# =============================
# PATH CONFIGURATION
# =============================

BASE_DIR = Path(__file__).resolve().parent.parent
input_path = BASE_DIR / "03_output" / "clean_shopee_products.csv"
output_path = BASE_DIR / "03_output" / "market_scoring_report.txt"

# =============================
# LOAD DATA
# =============================

df = pd.read_csv(input_path)

# Safety check
if df.empty:
    raise ValueError("Dataset is empty. Cannot compute market scoring.")

# =============================
# BASIC METRICS
# =============================

total_products = len(df)

# =============================
# PRICE SEGMENTATION
# =============================

bins = [0, 20000, 50000, 100000, 200000, 1000000]
labels = ["<20K", "20-50K", "50-100K", "100-200K", "200K+"]

df["price_range"] = pd.cut(df["price"], bins=bins, labels=labels)

price_dist = df["price_range"].value_counts().sort_index()

dominant_range = price_dist.idxmax()
dominant_count = price_dist.max()

# =============================
# SCORING CALCULATION
# =============================

# 1️⃣ Competition score (market density)
competition_score = min((total_products / 200) * 100, 100)

# 2️⃣ Saturation score (price clustering)
dominant_ratio = dominant_count / total_products
price_saturation_score = dominant_ratio * 100

# 3️⃣ Gap detection (low competition zones)
mean_distribution = price_dist.mean()
low_comp = price_dist[price_dist < mean_distribution]

gap_zone_factor = min(len(low_comp) * 10, 100)

# 4️⃣ Opportunity score (core formula)
opportunity_score = (
    (100 - competition_score) * 0.4 +
    (100 - price_saturation_score) * 0.4 +
    gap_zone_factor * 0.2
)

# 5️⃣ Market Attractiveness Index
market_index = opportunity_score - (competition_score * 0.3)

# =============================
# DAY 21 — CONFIDENCE LAYER
# =============================

confidence_score = min((total_products / 50) * 100, 100)

if confidence_score < 30:
    confidence_level = "LOW"
elif confidence_score < 70:
    confidence_level = "MEDIUM"
else:
    confidence_level = "HIGH"

adjusted_opportunity_score = opportunity_score * (confidence_score / 100)

# =============================
# SAVE REPORT
# =============================

report = f"""
=============================
MARKET SCORING MODEL REPORT
=============================

Total Products: {total_products}

-----------------------------
CORE SCORES
-----------------------------
Competition Score: {competition_score:.2f} / 100
Price Saturation Score: {price_saturation_score:.2f} / 100
Opportunity Score (Raw): {opportunity_score:.2f} / 100
Adjusted Opportunity Score: {adjusted_opportunity_score:.2f} / 100
Market Attractiveness Index: {market_index:.2f}

-----------------------------
PRICE ANALYSIS
-----------------------------
Dominant Price Range: {dominant_range}
Gap Zones: {", ".join(low_comp.index)}

-----------------------------
DATA CONFIDENCE
-----------------------------
Confidence Score: {confidence_score:.2f} / 100
Confidence Level: {confidence_level}

=============================
INTERPRETATION
=============================

Opportunity Score:
0–30   : Very weak opportunity
30–60  : Moderate opportunity
60–80  : Strong opportunity
80–100 : High potential market

Confidence Level:
LOW    : Insufficient data sample
MEDIUM : Moderate reliability
HIGH   : Strong data reliability

NOTE:
Use Adjusted Opportunity Score when confidence is LOW.

=============================
"""

with open(output_path, "w", encoding="utf-8") as f:
    f.write(report)

print("Market scoring report generated successfully.")