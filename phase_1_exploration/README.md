# Phase 1 — Exploration & Constraint Discovery (Day 1–7)

## Overview
Phase ini merupakan tahap eksplorasi awal untuk memahami **aksesibilitas data Shopee**, batasan teknis platform, serta kelayakan pendekatan scraping berbasis request/API untuk kebutuhan data bisnis.

Fokus utama bukan pada volume data, melainkan pada **pemahaman struktur sistem, perilaku proteksi, dan batas realistis ekstraksi data**.

---

## Objectives
- Mempelajari struktur halaman dan data Shopee
- Menguji kelayakan HTML scraping vs API-based extraction
- Mengidentifikasi pagination dan parameter pencarian
- Mengamati respon proteksi platform (rate limit, blocking, anti-bot)
- Mendokumentasikan pendekatan yang **tidak layak** untuk produksi

---

## Scope of Exploration
- Single product page scraping
- Search result pagination
- Internal API discovery via browser network inspection
- Request-based data extraction (non-authenticated)

---

## Key Findings

### 1. HTML Scraping Limitation
- Konten produk dan hasil pencarian **dirender secara dinamis (JavaScript)**
- HTML response kosong atau tidak mengandung data utama
- BeautifulSoup tidak efektif untuk data inti

**Conclusion:**  
HTML scraping langsung tidak viable.

---

### 2. Internal API Accessibility
- Internal API Shopee teridentifikasi melalui Network tab
- Endpoint mengembalikan data terstruktur (JSON)
- Pagination logic dapat dipahami

Namun:
- Request langsung menghasilkan **403 Forbidden**
- Session, token, dan fingerprint divalidasi secara ketat
- Manual header/cookie injection tidak cukup

**Conclusion:**  
Internal API **protected by active anti-bot mechanisms**.

---

### 3. Pagination & Search Logic
- Parameter `newest`, `limit`, dan `keyword` teridentifikasi
- Logika pagination dapat dipetakan secara konseptual
- Eksekusi tetap diblokir pada request-level

**Conclusion:**  
Pagination logic diketahui, tetapi **tidak dapat dieksekusi secara aman via direct requests**.

---

## Final Assessment

| Aspect | Result |
|------|-------|
| HTML scraping | ❌ Not viable |
| API direct access | ❌ Blocked (403) |
| Token replay | ❌ Not stable / unsafe |
| Request-based engine | ❌ Not production-ready |

---

## Strategic Conclusion
Pendekatan **request-level scraping** terhadap Shopee:
- Tidak stabil
- Tidak repeatable
- Tidak aman untuk kebutuhan klien

Phase ini berhasil mengidentifikasi bahwa:
> **Pendekatan eksploratif perlu dihentikan sebelum masuk ke jalur ilegal atau tidak defensible.**

---

## Next Phase
Hasil dari Phase 1 menjadi dasar untuk **Phase 2 — Market Intelligence Engine**, dengan pendekatan:
- Legal-compliant
- Browser-rendered data
- Focus on business insights, not endpoint exploitation
- Repeatable & client-ready

---

## Disclaimer
Phase ini bersifat eksploratif dan edukatif.  
Tidak digunakan untuk produksi, komersialisasi, atau bypass sistem proteksi platform.

All findings are documented for learning, architectural decision-making, and system design evolution.
