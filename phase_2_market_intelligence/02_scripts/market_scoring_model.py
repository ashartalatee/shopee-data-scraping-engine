import pandas as pd


def calculate_market_score(df: pd.DataFrame):
    if df.empty:
        raise ValueError("Dataset is empty. Cannot compute market scoring.")

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

    competition_score = min((total_products / 200) * 100, 100)

    dominant_ratio = dominant_count / total_products
    price_saturation_score = dominant_ratio * 100

    mean_distribution = price_dist.mean()
    low_comp = price_dist[price_dist < mean_distribution]

    gap_zone_factor = min(len(low_comp) * 10, 100)

    opportunity_score = (
        (100 - competition_score) * 0.4 +
        (100 - price_saturation_score) * 0.4 +
        gap_zone_factor * 0.2
    )

    market_index = opportunity_score - (competition_score * 0.3)

    # =============================
    # CONFIDENCE LAYER
    # =============================

    confidence_score = min((total_products / 50) * 100, 100)

    if confidence_score < 30:
        confidence_level = "LOW"
    elif confidence_score < 70:
        confidence_level = "MEDIUM"
    else:
        confidence_level = "HIGH"

    adjusted_opportunity_score = opportunity_score * (confidence_score / 100)

    return {
        "total_products": total_products,
        "competition_score": round(competition_score, 2),
        "price_saturation_score": round(price_saturation_score, 2),
        "opportunity_score": round(opportunity_score, 2),
        "adjusted_opportunity_score": round(adjusted_opportunity_score, 2),
        "market_index": round(market_index, 2),
        "dominant_price_range": str(dominant_range),
        "gap_zones": list(low_comp.index),
        "confidence_score": round(confidence_score, 2),
        "confidence_level": confidence_level
    }


# =============================
# OPTIONAL: STANDALONE MODE
# =============================
if __name__ == "__main__":
    from pathlib import Path

    BASE_DIR = Path(__file__).resolve().parent.parent
    input_path = BASE_DIR / "03_output" / "clean_shopee_products.csv"
    output_path = BASE_DIR / "03_output" / "market_scoring_report.txt"

    df = pd.read_csv(input_path)

    result = calculate_market_score(df)

    report = f"""
=============================
MARKET SCORING MODEL REPORT
=============================

Total Products: {result['total_products']}

Competition Score: {result['competition_score']} / 100
Price Saturation Score: {result['price_saturation_score']} / 100
Opportunity Score: {result['opportunity_score']} / 100
Adjusted Opportunity Score: {result['adjusted_opportunity_score']} / 100
Market Attractiveness Index: {result['market_index']}

Dominant Price Range: {result['dominant_price_range']}
Gap Zones: {", ".join(result['gap_zones'])}

Confidence Score: {result['confidence_score']} / 100
Confidence Level: {result['confidence_level']}
"""

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report)

    print("Market scoring report generated successfully.")