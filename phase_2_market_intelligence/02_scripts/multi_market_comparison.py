import pandas as pd
from market_scoring_model import calculate_market_score

results = []

keywords = ["botol minum", "tumbler", "botol olahraga"]

for kw in keywords:
    print(f"Analyzing: {kw}")

    df = pd.read_csv("03_output/clean_shopee_products.csv")

    result = calculate_market_score(df)

    result["keyword"] = kw

    results.append(result)

final_df = pd.DataFrame(results)