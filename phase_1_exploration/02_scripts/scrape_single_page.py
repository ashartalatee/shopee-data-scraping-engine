import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

URL = "https://shopee.co.id/Storex-Botol-Air-Minum-Jumbo-2-Liter-Botol-Air-Motivasi-Transparan-Botol-Air-Minum-Bening-BPA-FREE-i.1551015386.44551035359"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

product_name = soup.select_one("h1")
product_name_text = product_name.get_text(strip=True) if product_name else None

df = pd.DataFrame([{
    "product_name": product_name_text,
    "source_url": URL,
    "scraped_at": datetime.now().isoformat()
}])

df.to_excel("01_raw_data/single_page/produk_shopee_raw.xlsx", index=False)

print("HARI 3 DONE ✅")
print(product_name_text)