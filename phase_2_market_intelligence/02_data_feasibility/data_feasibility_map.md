# Data Feasibility Map – Market Intelligence

## Scope
Platform: Shopee Indonesia  
Kategori: Botol Minum  
Tujuan: Menilai kelayakan pengumpulan data untuk kebutuhan bisnis.

---

## 1. Market Demand

| Business Question | Data Needed | Data Type | Source | Collection Method | Risk Level |
|------------------|------------|-----------|--------|-------------------|------------|
| Jumlah listing aktif | Total produk di hasil pencarian | Count | Halaman pencarian | Manual sampling / crawl ringan | Low |
| Produk dominan | Judul produk | Text | Halaman pencarian | Manual review | Low |

---

## 2. Pricing Intelligence

| Business Question | Data Needed | Data Type | Source | Collection Method | Risk Level |
|------------------|------------|-----------|--------|-------------------|------------|
| Rentang harga pasar | Harga produk | Numeric | Listing publik | Manual sampling | Low |
| Harga median | Harga + posisi | Numeric | Listing publik | Estimasi statistik | Low |

---

## 3. Competition

| Business Question | Data Needed | Data Type | Source | Collection Method | Risk Level |
|------------------|------------|-----------|--------|-------------------|------------|
| Jumlah seller unik | Nama toko | Text | Listing publik | Parsing visual | Low |
| Dominasi seller | Frekuensi kemunculan toko | Count | Listing publik | Aggregasi | Medium |

---

## 4. Product Feature Signals

| Business Question | Data Needed | Data Type | Source | Collection Method | Risk Level |
|------------------|------------|-----------|--------|-------------------|------------|
| Fitur populer | Kata kunci judul | Text | Judul produk | Text analysis | Low |
| Klaim produk | Deskripsi singkat | Text | Listing publik | Manual extract | Medium |

---

## 5. Trust & Social Proof

| Business Question | Data Needed | Data Type | Source | Collection Method | Risk Level |
|------------------|------------|-----------|--------|-------------------|------------|
| Review threshold | Jumlah review | Numeric | Listing publik | Sampling | Medium |
| Rating dominan | Rating produk | Numeric | Listing publik | Estimasi | Medium |

---

## 6. Risk Notes

- Tidak menggunakan endpoint private atau reverse-engineered.
- Tidak menyimpan data personal user.
- Fokus pada data agregat & publik.
- Estimasi digunakan jika data real-time tidak tersedia.

---

## 7. Professional Positioning

Dokumen ini digunakan untuk:
- Menjelaskan batasan teknis ke klien
- Melindungi engineer dari permintaan berisiko
- Menentukan scope & harga layanan
