# ==========================================================
# Nama    : Muhammad Najmi Khoiri Almunawwar
# NIM     : J0403251095
# Kelas   : TPL B
# Judul   : Praktikum 13 - Latihan 4: Studi Kasus Jaringan Kabel Kampus
# Modul   : Modul 9 - Graph III: Spanning Trees
# Matkul  : Algoritma dan Struktur Data (TPL2106)
# ==========================================================
#
# Kasusnya: kampus mau masang kabel internet ke semua gedung
# tapi pengen biaya pemasangannya semurah mungkin.

# - Kita mau semua gedung nyambung (spanning)
# - Dengan biaya total yang seminim mungkin (minimum)
# - Nggak perlu bikin jalur kabel yang "muter" (no cycle)
# Di sini kita pakai Prim .
# ==========================================================

import heapq

# Graph gedung-gedung kampus
# Bobot = biaya pasang kabel (dalam satuan jutaan rupiah misalnya)
graph = {
    'GedungA': {'GedungB': 4, 'GedungC': 2, 'GedungD': 5},
    'GedungB': {'GedungA': 4, 'GedungD': 3},
    'GedungC': {'GedungA': 2, 'GedungD': 1},
    'GedungD': {'GedungA': 5, 'GedungB': 3, 'GedungC': 1}
}

# Semua koneksi yang mungkin ada (sebelum MST):
# GedungA - GedungB = 4 juta
# GedungA - GedungC = 2 juta
# GedungB - GedungD = 3 juta
# GedungC - GedungD = 1 juta  ← ini yang paling murah
# GedungA - GedungD = 5 juta


def prim(graph, start):
    """
    Jalanin algoritma Prim buat nyari MST.
    Mulai dari gedung 'start', terus sambungin ke gedung
    tetangga yang paling murah biaya kabelnya.
    """
    visited = set([start])    # gedung yang udah "terpasang kabel"
    edges = []                 # kandidat kabel yang bisa dipasang berikutnya
    mst = []                   # kabel-kabel yang akhirnya dipasang
    total_biaya = 0            # total biaya kabel yang dipasang

    # masukkan semua gedung tetangga dari gedung awal ke antrian
    for tetangga, biaya in graph[start].items():
        heapq.heappush(edges, (biaya, start, tetangga))

    while edges:
        # pilih jalur kabel yang paling murah saat ini
        biaya, dari_gedung, ke_gedung = heapq.heappop(edges)

        # kalau gedung tujuan udah punya kabel, skip (nggak perlu dobel)
        if ke_gedung not in visited:
            visited.add(ke_gedung)
            mst.append((dari_gedung, ke_gedung, biaya))
            total_biaya += biaya

            # dari gedung yang baru dipasang kabel,
            # lihat gedung-gedung tetangganya yang belum kena kabel
            for tetangga, b in graph[ke_gedung].items():
                if tetangga not in visited:
                    heapq.heappush(edges, (b, ke_gedung, tetangga))

    return mst, total_biaya


# mulai pasang kabel dari GedungA
mst, total = prim(graph, 'GedungA')

print("=" * 50)
print("  Latihan 4: Jaringan Kabel Antar Gedung Kampus")
print("=" * 50)
print("Jalur kabel yang dipilih (biaya minimum):\n")
for dari, ke, biaya in mst:
    print(f"  {dari} ──── {ke}   (biaya: {biaya})")

print(f"\nTotal biaya pemasangan kabel = {total}")
print(f"(Semua {len(graph)} gedung sudah terhubung dengan {len(mst)} jalur kabel)")


# ==========================================================
# JAWABAN ANALISIS
# ==========================================================

# 1. Algoritma apa yang digunakan?
#    - Prim. Kita pilih Prim karena graph ini relatif dense
#      (banyak koneksi antar gedung), dan Prim bagus buat kasus gitu.
#      Tapi sebenernya Kruskal juga bisa dan hasilnya sama.

# 2. Edge mana saja yang dipilih?
#    - GedungA - GedungC (biaya 2)
#      GedungC - GedungD (biaya 1)
#      GedungD - GedungB (biaya 3)
#    Total 3 jalur untuk 4 gedung → sesuai rumus N-1 edge.

# 3. Berapa total biaya minimum?
#    - Total = 2 + 1 + 3 = 6 (satuan biaya)
#      Ini yang paling murah dari semua kemungkinan yang ada.
#      Kalau kita asal-asalan pilih jalur, bisa jauh lebih mahal.

# 4. Mengapa MST cocok digunakan pada kasus ini?
#    - Karena masalahnya persis cocok sama definisi MST:
#      - Mau nyambungin SEMUA gedung (spanning)
#      - Dengan biaya SEKECIL MUNGKIN (minimum)
#      - Nggak perlu jalur kabel yang redundan/dobel (no cycle)
#
#      MST kasih kita solusi optimal: pasang kabel sesedikit mungkin
#      tapi tetap bisa nyambungin semua gedung. Efisien banget!
# ==========================================================
