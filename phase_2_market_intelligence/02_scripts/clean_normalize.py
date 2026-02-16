import pandas as pd
import re
from pathlib import Path

# base directory phase_2_market_intelligence
BASE_DIR = Path(__file__).resolve().parent.parent

# input
input_path = BASE_DIR / "03_output" / "raw_sample.csv"
df = pd.read_csv(input_path)

# drop baris kosong
df = df.dropna(subset=["title", "url"])

# normalisasi title
df["title_clean"] = (
    df["title"]
    .str.lower()
    .str.replace(r"\s+", " ", regex=True)
    .str.strip()
)

# ekstrak kapasitas (contoh: 2L, 2000ml)
def extract_capacity(text):
    if not isinstance(text, str):
        return None

    ml = re.search(r"(\d{3,4})\s*ml", text)
    liter = re.search(r"(\d+(\.\d+)?)\s*l", text)

    if ml:
        return int(ml.group(1))
    if liter:
        return int(float(liter.group(1)) * 1000)

    return None

df["capacity_ml"] = df["title_clean"].apply(extract_capacity)

# flag kategori
df["is_botol_minum"] = df["title_clean"].str.contains("botol")

# output
output_path = BASE_DIR / "03_output" / "clean_shopee_products.csv"
df.to_csv(output_path, index=False)

print("HARI 13 DONE")
print(df.head())
