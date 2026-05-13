# ==========================================================
# Nama    : Muhammad Najmi Khoiri Almunawwar
# NIM     : J0403251095
# Kelas   : TPL B
# Judul   : Praktikum 13 - Latihan 5: Tugas Mandiri MST Jaringan Komputer

# ==========================================================

# ==========================================================
# REPRESENTASI GRAPH
# Format edge: (bobot, router_asal, router_tujuan)
# Kruskal butuh list of edges, bukan nested dictionary
# ==========================================================
edges = [
    (3, 'RouterA', 'RouterB'),   # A ke B cost 3
    (2, 'RouterA', 'RouterC'),   # A ke C cost 2
    (5, 'RouterB', 'RouterD'),   # B ke D cost 5, ini yang paling mahal
    (1, 'RouterC', 'RouterD'),   # C ke D cost 1, ini yang paling murah!
    (4, 'RouterB', 'RouterC')    # B ke C cost 4
]

# semua node yang ada di jaringan ini
all_routers = {'RouterA', 'RouterB', 'RouterC', 'RouterD'}


def kruskal(edges, nodes):
    """
    Fungsi Kruskal untuk nyari MST.
    Cara kerjanya:
    1. Sort semua edge dari yang termurah
    2. Ambil satu-satu, skip kalau bakal bikin cycle
    3. Berhenti pas semua node udah nyambung
    """

    # urutin edge dari bobot terkecil ke terbesar
    sorted_edges = sorted(edges)

    mst = []
    total_cost = 0
    connected = set()   # router-router yang udah masuk MST

    print("Proses pemilihan edge:")

    for cost, u, v in sorted_edges:
        # cek apakah edge ini aman (nggak bikin cycle)
        if u not in connected or v not in connected:
            mst.append((u, v, cost))
            total_cost += cost
            connected.add(u)
            connected.add(v)
            print(f"  ✓ Pilih  {u} -- {v}  (cost: {cost})")

            # kalau semua node udah terhubung, bisa berhenti
            if connected == nodes:
                break
        else:
            print(f"  ✗ Skip   {u} -- {v}  (cost: {cost}) → cycle!")

    return mst, total_cost


# jalankan!
mst, total = kruskal(edges, all_routers)

print("\n" + "=" * 50)
print("  Latihan 5: Jaringan Komputer - Hasil MST")
print("=" * 50)
print("Edge yang masuk ke MST (Kruskal):\n")
for u, v, cost in mst:
    print(f"  {u} ←→ {v}   (cost: {cost})")

print(f"\nTotal biaya minimum = {total}")
print(f"Jumlah koneksi yang dipasang = {len(mst)}")
print(f"(Dari {len(all_routers)} router, butuh {len(all_routers)-1} koneksi)")


# ==========================================================
# JAWABAN ANALISIS
# ==========================================================

# 1. Kasus apa yang dipilih?
#    - Kasus 2: Jaringan Komputer dengan 4 router (RouterA, B, C, D).
#      Kasusnya nyambungin semua router dengan total biaya koneksi
#      yang paling kecil.

# 2. Algoritma apa yang digunakan?
#    - Kruskal. Dipilih karena graph ini sparse (5 edge untuk 4 node)
#      dan Kruskal cocok buat graph yang jumlah edge-nya nggak terlalu banyak.
#      Selain itu Kruskal logikanya mudah dipahami: sort dulu, pilih satu-satu.

# 3. Edge mana saja yang dipilih dalam MST?
#    - Urutan pemilihan Kruskal:
#      1. RouterC - RouterD (cost 1) - terkecil, ambil
#      2. RouterA - RouterC (cost 2) - ambil
#      3. RouterA - RouterB (cost 3) - ambil
#      Semua 4 router udah nyambung dengan 3 koneksi.
#
#      Edge yang di-skip:
#      - RouterB - RouterC (cost 4) - bakal bikin cycle A-C-B-A
#      - RouterB - RouterD (cost 5) - bakal bikin cycle juga

# 4. Berapa total bobot MST?
#    - Total = 1 + 2 + 3 = 6
#      Ini biaya minimum untuk nyambungin semua 4 router.
#      Kalau asal pilih koneksi tanpa MST, bisa habis lebih banyak.

# 5. Mengapa edge tertentu tidak dipilih?
#    - RouterB - RouterC (4) dan RouterB - RouterD (5) nggak dipilih
#      karena saat giliran mereka diproses, kedua ujung node-nya
#      udah dua-duanya ada di 'connected'.
#
#      Kalau dipaksa diambil, bakal bikin siklus:
#      - B-C diambil - terbentuk siklus: A - C - B - A
#      - B-D diambil - terbentuk siklus: C - D - (via B)
#
#      Kruskal pintar skip ini karena siklus = buang-buang biaya
#      tanpa nambah konektivitas apapun.
# ==========================================================
