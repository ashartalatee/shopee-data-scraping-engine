import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
input_path = BASE_DIR / "03_output" / "clean_shopee_products.csv"

df = pd.read_csv(input_path)

print("\n=== BASIC OVERVIEW ===")
print("Total Produk:", len(df))
print("Rata-rata Harga:", round(df["price"].mean(), 2))
print("Median Harga:", df["price"].median())


# 1️⃣ PRICE RANGE BUCKETING


bins = [0, 20000, 50000, 100000, 200000, 1000000]
labels = ["<20K", "20-50K", "50-100K", "100-200K", "200K+"]

df["price_range"] = pd.cut(df["price"], bins=bins, labels=labels)

price_distribution = df["price_range"].value_counts().sort_index()

print("\n=== PRICE DISTRIBUTION ===")
print(price_distribution)


# 2️⃣ CAPACITY DOMINANCE


capacity_distribution = df["capacity_ml"].value_counts().sort_index()

print("\n=== CAPACITY DISTRIBUTION (ml) ===")
print(capacity_distribution)


# 3️⃣ AVERAGE PRICE PER CAPACITY


avg_price_capacity = (
    df.groupby("capacity_ml")["price"]
    .mean()
    .round(2)
    .sort_index()
)

print("\n=== AVG PRICE PER CAPACITY ===")
print(avg_price_capacity)


# SAVE SIGNAL REPORT


output_path = BASE_DIR / "03_output" / "market_signal_summary.csv"

summary = df.groupby("capacity_ml").agg(
    total_products=("title", "count"),
    avg_price=("price", "mean")
).reset_index()

summary.to_csv(output_path, index=False)

print("\nHARI 14 DONE ✅")
