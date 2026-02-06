# Phase 2 — Market Intelligence Design (Day 8)

## Objective
Membangun sistem Market Intelligence sederhana untuk membantu seller
memahami:
- posisi harga pasar
- perubahan harga kompetitor
- peluang penyesuaian strategi jual

Fokus phase ini adalah **desain sistem**, bukan scraping teknis.

---

## Business Question
Masalah bisnis yang ingin dijawab:

1. Berapa rentang harga produk sejenis di pasar?
2. Apakah harga kompetitor naik atau turun dari waktu ke waktu?
3. Produk mana yang konsisten murah / mahal?

---

## Target Market Simulation
Simulasi klien:
- Seller Shopee kategori botol minum
- Skala UMKM
- Tidak paham teknis
- Butuh data dalam Excel

---

## Data Fields (Planned)
Field yang bernilai bisnis:

- product_name
- price
- shop_name
- rating
- sold
- scraped_date
- source (search / category)

Field yang **tidak diambil**:
- deskripsi panjang
- gambar
- detail UI

---

## Data Source Strategy (Legal & Stable)
Pendekatan yang digunakan:
- Browser-rendered data
- Manual export / semi-automated
- Publicly visible information
- No API exploitation
- No bypass protection

---

## Output Expectation
Klien menerima:
- File Excel rapi
- Bisa difilter & dibandingkan
- Siap dipakai tanpa Python

---

## Success Criteria
Phase ini dianggap berhasil jika:
- Tujuan bisnis jelas
- Field data jelas
- Alur data masuk akal
- Siap diimplementasikan secara aman
