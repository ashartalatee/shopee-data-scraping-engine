import pandas as pd
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
input_path = BASE_DIR / "03_output" / "clean_shopee_products.csv"
df = pd.read_csv(input_path)

# Filter kategori botol minum
df = df[df["is_botol_minum"]]

# Buat bucket harga
price_bins = [0, 20000, 50000, 100000, 200000, 1000000]
price_labels = ["<20K", "20-50K", "50-100K", "100-200K", "200K+"]
df["price_range"] = pd.cut(df["price"], bins=price_bins, labels=price_labels)

# Buat bucket kapasitas
capacity_bins = [0, 250, 500, 1000, 2000, 5000]
capacity_labels = ["<250ml", "250-500ml", "500-1000ml", "1-2L", "2L+"]
df["capacity_range"] = pd.cut(df["capacity_ml"], bins=capacity_bins, labels=capacity_labels)

# Grid matrix
grid = df.groupby(["capacity_range", "price_range"]).agg(
    product_count=("title_clean", "count"),
    avg_price=("price", "mean")
).reset_index()

# Normalisasi kompetisi & scoring peluang
max_count = grid["product_count"].max()
grid["competition_score"] = 1 - (grid["product_count"] / max_count)

# Opportunity Score = competition_score (tinggi) x avg_price (indikasi revenue)
grid["opportunity_score"] = grid["competition_score"] * grid["avg_price"]

# Urutkan descending berdasarkan opportunity_score
grid_sorted = grid.sort_values("opportunity_score", ascending=False)

# Simpan hasil
grid_sorted.to_csv(BASE_DIR / "03_output/market_gap_opportunity.csv", index=False)

print("HARI 16 DONE")
print(grid_sorted.head(10))
