# Shopee Data Scraping Engine  
## Phase 1 — Exploration & Constraint Discovery (Day 1–7)

Phase ini bertujuan **bukan untuk menghasilkan data produksi**,  
melainkan untuk **memahami batas teknis, struktur data, dan proteksi platform Shopee**  
sebagai fondasi sebelum membangun engine market intelligence yang profesional.

---

## Objective Phase 1

- Memahami struktur halaman dan data Shopee
- Mengidentifikasi field data bernilai bisnis
- Menguji kelayakan pendekatan scraping berbasis request
- Menemukan batas dan constraint nyata dari platform
- Menarik kesimpulan teknis yang dapat dipertanggungjawabkan

---

## Daily Log & Findings

### Day 1 — Platform Observation
- Observasi struktur halaman produk Shopee
- Identifikasi data yang terlihat oleh user (nama produk, harga, rating, dll)
- Memahami bahwa konten dirender secara dinamis (JavaScript-heavy)
- **Belum ada scraping**, fokus pemetaan struktur & konteks

 Insight:
HTML statis tidak merepresentasikan data final yang dilihat user.

---

### Day 2 — Business-Oriented Data Selection
- Menentukan field data bernilai bisnis (bukan semua field)
- Menyusun data dictionary awal
- Fokus pada *decision-useful data*, bukan kuantitas

Field awal:
- product_name
- price
- sold
- rating
- shop_name
- source_url
- scraped_at

 Insight:
Nilai data ditentukan oleh **kegunaan bisnis**, bukan kelengkapan teknis.

---

### Day 3 — Single Page Scraping (Proof of Concept)
- Scraping 1 halaman produk (URL hardcoded)
- Menggunakan `requests + BeautifulSoup`
- Fokus validasi pipeline dasar (request → parse → output)
- Output ke Excel sebagai raw data

 Result:
- Pipeline berjalan
- Namun data utama (product_name) tidak terbaca → `None`

 Insight:
Data utama **tidak tersedia di HTML statis**.

---

### Day 4 — Internal API Discovery
- Analisis network request via browser DevTools
- Identifikasi internal API Shopee (search & product endpoints)
- Memahami parameter pagination (`newest`, `limit`)
- Menguji endpoint via curl

 Insight:
Shopee menggunakan API internal yang **tidak ditujukan untuk public access**.

---

### Day 5 — Search Pagination Attempt
- Implementasi script pagination berbasis API internal
- Percobaan scraping search result per halaman
- Hasil: data kosong / tidak konsisten

 Insight:
Akses API search tidak stabil dan tidak dapat diandalkan untuk produksi.

---

### Day 6 — Anti-Bot Enforcement Encounter
- Request ke API search mulai konsisten mendapat status **403**
- Penambahan header, cookies, session tidak membantu
- Deteksi proteksi aktif (anti-bot / anti-scraping)

 Insight:
Pendekatan request-based scraping **diblokir secara sistematis**.

---

### Day 7 — Constraint Conclusion & Architecture Decision
- Evaluasi seluruh pendekatan Phase 1
- Menarik kesimpulan teknis berbasis eksperimen nyata

Kesimpulan:
- HTML scraping ❌ (JS-rendered)
- Direct API access ❌ (protected & unstable)
- Request-level scraping ❌ (403 enforcement)

 Final Insight:
Pendekatan scraping berbasis request **tidak layak untuk engine profesional**.

---

## Phase 1 Conclusion

Phase 1 berhasil:
- Mengungkap batas teknis platform Shopee
- Menghindari jebakan solusi “katanya bisa”
- Menjadi dasar keputusan arsitektur yang rasional

Phase ini **tidak gagal**,  
justru **menghemat waktu dan risiko jangka panjang**.

---

## Next Phase

**Phase 2 — Market Intelligence Engine (Legal & Repeatable)**  
Pendekatan akan beralih ke:
- Browser-rendered data
- Visible & user-level information
- Strategic sampling & business insight extraction
- Engine yang aman, stabil, dan client-ready
