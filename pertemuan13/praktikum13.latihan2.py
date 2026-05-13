# ==========================================================
# Nama    : Muhammad Najmi Khoiri Almunawwar
# NIM     : J0403251095
# Kelas   : TPL B
# Judul   : Praktikum 13 - Latihan 2: Implementasi Kruskal
# ==========================================================

edges = [
    (1, 'C', 'D'),   # paling murah!
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')    # paling mahal
]

# Step pertama Kruskal: urutin semua edge dari yang termurah
# Python sort tuple itu otomatis ngurut dari elemen pertama (bobot)
edges.sort()

mst = []          # edge-edge yang masuk MST bakal disimpen di sini
total_weight = 0  # total bobot MST

# connected = node-node yang udah "bergabung" ke MST
# awalnya kosong, diisi pas kita pilih edge
connected = set()

print("=" * 45)
print("  Latihan 2: Kruskal - Proses Pemilihan Edge")
print("=" * 45)
print("\nUrutan edge setelah di-sort (terkecil → terbesar):")
for w, u, v in edges:
    print(f"  {u}-{v} (bobot {w})")

print("\n--- Proses Kruskal ---")

for weight, u, v in edges:

    # cek apakah edge ini aman ditambah
    # kalau setidaknya salah satu node belum ada di connected,
    # kita aman ambil edge ini (nggak bakal bikin cycle)
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight
        connected.add(u)
        connected.add(v)
        print(f"  ✓ Pilih edge {u}-{v} (bobot {weight}) → connected: {connected}")
    else:
        # kedua node udah nyambung → kalau diambil bakal bikin cycle
        print(f"  ✗ Skip edge {u}-{v} (bobot {weight}) → akan bentuk cycle!")

print("\n--- Hasil MST ---")
print("Edge yang masuk MST:")
for u, v, w in mst:
    print(f"  {u} -- {v}  (bobot: {w})")
print(f"\nTotal bobot MST = {total_weight}")


# ==========================================================
# JAWABAN ANALISIS
# ==========================================================

# 1. Edge mana yang dipilih pertama kali?
#    - Edge C-D dengan bobot 1. Ini yang paling kecil bobotnya
#      di antara semua edge yang ada, jadi Kruskal langsung pilih ini.

# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
#    - Karena tujuan MST adalah total bobot MINIMUM.
#      Logika Kruskal: kalau kita selalu pilih yang termurah duluan
#      dan nggak bikin cycle, hasilnya pasti bakal total minimum.
#      Ini namanya pendekatan greedy — ambil yang terbaik di tiap langkah.

# 3. Berapa total bobot MST yang dihasilkan?
#    - Total = 1 (C-D) + 2 (A-C) + 3 (B-D) = 6

# 4. Mengapa edge tertentu tidak dipilih?
#    - Edge A-B (bobot 4) dan A-D (bobot 5) nggak dipilih karena
#      saat giliran mereka diproses, kedua ujung node-nya (A & B,
#      A & D) udah dua-duanya masuk ke 'connected'.
#      Artinya kalau dipaksa diambil, bakal bikin cycle di MST.
#      Kruskal bijak, dia skip aja edge-edge kayak gini.
# ==========================================================
