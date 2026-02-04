from playwright.sync_api import sync_playwright
import pandas as pd
from datetime import datetime

data = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://shopee.co.id/search?keyword=botol%20minum", timeout=60000)

    page.wait_for_selector("div[data-sqe='item']", timeout=60000)

    items = page.query_selector_all("div[data-sqe='item']")

    for item in items[:20]:
        try:
            name = item.query_selector("div._1NoI8_").inner_text()
            price = item.query_selector("span._341bF0").inner_text()
            sold = item.inner_text().split("terjual")[0].split()[-1]

            data.append({
                "name": name,
                "price": price,
                "sold": sold,
                "scraped_at": datetime.now().isoformat()
            })
        except:
            continue

    browser.close()

df = pd.DataFrame(data)
df.to_excel(
    "01_raw_data/search/shopee_search_botol_minum.xlsx",
    index=False
)

print("HARI 5 DONE ✅")
print(df.head())
