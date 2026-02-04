
---
## Data Scraping Freelance — Shopee Case

## Project Overview

Project ini adalah **end-to-end Data Scraping & Market Monitoring Engine** menggunakan **Shopee** sebagai studi kasus.

Tujuan utama project:

* Mengambil data pasar e-commerce secara terstruktur
* Membersihkan & menstandarkan data agar siap dianalisis
* Melakukan monitoring perubahan harga dari waktu ke waktu
* Menyediakan output yang **siap dipakai bisnis (Excel-based)**

Project ini dirancang dengan mindset **freelancer profesional**, bukan eksperimen sekali jalan.

---

## Use Case Nyata

Project ini relevan untuk:

* Seller Shopee / Tokopedia
* Brand owner
* Market researcher
* Competitive pricing analyst

Contoh kebutuhan klien:

* "Saya ingin tahu harga kompetitor setiap hari"
* "Produk mana yang stabil / sering diskon"
* "Bagaimana tren harga dalam 7–30 hari"

---

## Struktur Output Utama

| File                            | Fungsi                     | Dipakai Oleh     |
| ------------------------------- | -------------------------- | ---------------- |
| `produk_shopee_raw.xlsx`        | Data mentah hasil scraping | Audit / Debug    |
| `produk_shopee_clean.xlsx`      | Data bersih siap analisis  | Seller / Analyst |
| `monitoring_harga.xlsx`         | Perubahan harga per waktu  | Decision Maker   |
| `monitoring_harga_summary.xlsx` | Insight ringkas            | Owner / Manager  |
| `error_log.txt`                 | Catatan error              | Developer / QA   |

---

## Teknologi & Tools

* Python
* Requests / Playwright / Selenium (opsional)
* Pandas
* Excel (sebagai format deliverable utama)

> Catatan: Excel dipilih karena **95% klien non-teknis menggunakannya**.

---

## Cara Menjalankan Project

1. Clone repository
2. Install dependency:

   ```bash
   pip install -r requirements.txt
   ```
3. Jalankan script sesuai kebutuhan:

   * Scrape 1 halaman → `scrape_single_page.py`
   * Scrape kategori → `scrape_category_pagination.py`
   * Cleaning data → `data_cleaning.py`
   * Update monitoring → `update_monitoring.py`

---

## Prinsip Desain

Project ini dibangun dengan prinsip:

* Data mentah **tidak ditimpa**
* Script **boleh error, tapi tidak boleh mati total**
* Output harus bisa dipahami **tanpa membaca kode**

---

## Tentang Developer

Project ini dibuat sebagai simulasi kerja **Data Extraction / Market Monitoring Freelancer**.

Fokus utama:

* Akurasi data
* Kerapian output
* Kesiapan dipakai bisnis

---

# workflow.md (Alur Kerja Profesional)

## Observasi & Targeting

* Menentukan halaman produk / kategori Shopee
* Identifikasi field penting (nama, harga, rating, sold)

*Kenapa penting:* bisnis tidak butuh semua data, hanya data bernilai.

---

## Data Extraction (Scraping)

* Scraping single page untuk validasi struktur
* Scraping kategori dengan pagination
* Delay & header diterapkan agar stabil

*Relevansi nyata:* klien sering minta ratusan produk sekaligus.

---

## Raw Data Validation

* Cek jumlah baris
* Cek missing value
* Simpan sebagai **raw data (tidak diubah)**

*Kenapa:* raw data adalah bukti audit & cadangan.

---

## Data Cleaning & Normalization

* Harga → angka murni
* Kolom distandarkan
* Tipe data diperbaiki

*Relevansi:* data mentah tidak bisa langsung dianalisis.

---

## Update & Monitoring

* Scraping dijalankan ulang di hari berbeda
* Data lama vs baru dibandingkan
* Timestamp ditambahkan

*Nilai bisnis:* ini dasar **monitoring harga & retainer bulanan**.

---

## Error Handling & Logging

* Halaman gagal di-skip
* Error dicatat di `error_log.txt`

*Profesionalisme:* script tidak boleh mati hanya karena 1 error.

---

## Delivery ke Klien

* Output Excel rapi
* Insight ringkas (summary)
* Dokumentasi jelas

*Klien tidak membeli kode, mereka membeli kejelasan & keputusan.*

---

## Penutup

Workflow ini mencerminkan **alur kerja dunia nyata freelancer data**, bukan sekadar latihan teknis.

> Jika kamu bisa menjalankan workflow ini end-to-end, kamu **siap dijual ke klien**.
