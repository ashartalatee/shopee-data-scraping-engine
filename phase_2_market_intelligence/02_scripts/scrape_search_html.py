import requests
from datetime import datetime

URL = "https://shopee.co.id/search?keyword=botol%20minum"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(URL, headers=headers, timeout=15)

filename = f"shopee_search_raw_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"

with open(filename, "w", encoding="utf-8") as f:
    f.write(response.text)

print("HARI 12 DONE")
print("HTML saved as:", filename)
print("HTML length:", len(response.text))
