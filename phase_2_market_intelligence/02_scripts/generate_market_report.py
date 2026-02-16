import pandas as pd
from pathlib import Path
from datetime import datetime


# SETUP PATH


BASE_DIR = Path(__file__).resolve().parent.parent
input_path = BASE_DIR / "03_output" / "clean_shopee_products.csv"
output_path = BASE_DIR / "03_output" / "market_report.txt"

df = pd.read_csv(input_path)


# BASIC METRICS


total_products = len(df)
avg_price = df["price"].mean()


# PRICE DISTRIBUTION


bins = [0, 20000, 50000, 100000, 200000, 1000000]
labels = ["<20K", "20-50K", "50-100K", "100-200K", "200K+"]

df["price_range"] = pd.cut(df["price"], bins=bins, labels=labels)
price_dist = df["price_range"].value_counts().sort_index()

dominant_price = price_dist.idxmax()


# CAPACITY DISTRIBUTION


capacity_dist = df["capacity_ml"].value_counts().sort_index()
dominant_capacity = capacity_dist.idxmax()


# SIMPLE GAP DETECTION


low_competition = price_dist[price_dist < price_dist.mean()]
gap_zones = list(low_competition.index)


# VALIDATION CHECK


data_warning = ""

if total_products < 30:
    data_warning = (
        "WARNING: Sample size is very small. "
        "Insights may not represent actual market conditions.\n"
    )



# GENERATE NARRATIVE


report = f"""
=============================
SHOPEE MARKET INTELLIGENCE REPORT
Generated: {datetime.now().strftime("%Y-%m-%d %H:%M")}
=============================

TOTAL PRODUCTS ANALYZED:
{total_products}

AVERAGE PRICE:
Rp {avg_price:,.0f}

DOMINANT PRICE RANGE:
{dominant_price}

DOMINANT CAPACITY:
{dominant_capacity} ml

LOW COMPETITION PRICE ZONES:
{", ".join(gap_zones)}

-----------------------------
MARKET INSIGHT SUMMARY
-----------------------------

The market is currently dominated by products in the {dominant_price} range,
with most listings offering capacity around {dominant_capacity} ml.

Average product price sits at Rp {avg_price:,.0f},
indicating a mid-market positioning strategy.

Price zones with relatively lower competition:
{", ".join(gap_zones)}

These areas may represent potential entry opportunities,
depending on demand validation and differentiation strategy.

=============================
END OF REPORT
=============================
"""


# SAVE REPORT


with open(output_path, "w", encoding="utf-8") as f:
    f.write(report)

print("DAY 16 DONE")
print(f"Report saved to: {output_path}")
