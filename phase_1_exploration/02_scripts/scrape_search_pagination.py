import requests
import pandas as pd
from datetime import datetime
import time

URL = "https://shopee.co.id/api/v4/search/search_items"

KEYWORD = "botol minum"
LIMIT = 20
MAX_PAGES = 5

# 👇 PASTE COOKIE BROWSER KAMU DI SINI
COOKIE_STRING = "PASTE_COOKIE_DI_SINI"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Accept-Language": "id-ID,id;q=0.9",
    "Referer": "https://shopee.co.id/search?keyword=botol%20minum",
    "X-Requested-With": "XMLHttpRequest",
    "X-API-SOURCE": "pc"
}

session = requests.Session()
session.headers.update(headers)

# inject cookies
for item in COOKIE_STRING.split(";"):
    if "=" in item:
        k, v = item.strip().split("=", 1)
        session.cookies.set(k, v)

all_rows = []

for page in range(MAX_PAGES):
    newest = page * LIMIT
    print(f"Scraping page {page+1}, newest={newest}")

    params = {
        "by": "relevancy",
        "keyword": KEYWORD,
        "limit": LIMIT,
        "newest": newest,
        "order": "desc",
        "page_type": "search",
        "scenario": "PAGE_GLOBAL_SEARCH",
        "version": 2
    }

    r = session.get(URL, params=params, timeout=10)

    print("Status:", r.status_code)

    if r.status_code != 200:
        print("Blocked. Stop.")
        break

    items = r.json().get("items", [])

    if not items:
        print("No more items.")
        break

    for it in items:
        b = it.get("item_basic", {})
        all_rows.append({
            "keyword": KEYWORD,
            "name": b.get("name"),
            "price": b.get("price"),
            "sold": b.get("sold"),
            "rating": b.get("rating_star"),
            "shopid": b.get("shopid"),
            "itemid": b.get("itemid"),
            "scraped_at": datetime.now().isoformat()
        })

    time.sleep(2)

df = pd.DataFrame(all_rows)
df.to_excel("01_raw_data/search/shopee_search_day6.xlsx", index=False)

print("HARI 6 DONE ✅")
print("Total data:", len(df))
