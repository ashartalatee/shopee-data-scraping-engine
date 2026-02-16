import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Base directory (aman & portable)
BASE_DIR = Path(__file__).resolve().parent.parent
input_path = BASE_DIR / "03_output" / "clean_shopee_products.csv"

df = pd.read_csv(input_path)


# 1️⃣ PRICE DISTRIBUTION


bins = [0, 20000, 50000, 100000, 200000, 1000000]
labels = ["<20K", "20-50K", "50-100K", "100-200K", "200K+"]

df["price_range"] = pd.cut(df["price"], bins=bins, labels=labels)
price_distribution = df["price_range"].value_counts().sort_index()

plt.figure()
price_distribution.plot(kind="bar")
plt.title("Price Distribution")
plt.xlabel("Price Range")
plt.ylabel("Number of Products")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 2️⃣ CAPACITY DISTRIBUTION


capacity_distribution = df["capacity_ml"].value_counts().sort_index()

plt.figure()
capacity_distribution.plot(kind="bar")
plt.title("Capacity Distribution (ml)")
plt.xlabel("Capacity (ml)")
plt.ylabel("Number of Products")
plt.tight_layout()
plt.show()

print("HARI 15 DONE")
