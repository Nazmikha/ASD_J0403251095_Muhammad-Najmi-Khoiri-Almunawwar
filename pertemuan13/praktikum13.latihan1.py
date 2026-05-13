# ==========================================================
# Nama    : Muhammad Najmi Khoiri Almunawwar
# NIM     : J0403251095
# Kelas   : TPL B
# Judul   : Praktikum 13 - Latihan 1: Konsep Spanning Tree
# ==========================================================

edges = [
    ('A', 'B'),   # A nyambung ke B
    ('A', 'C'),   # A nyambung ke C
    ('A', 'D'),   # A nyambung ke D
    ('C', 'D'),   # C nyambung ke D
    ('B', 'D')    # B nyambung ke D
]
# Total ada 5 edge, tapi graph ini punya cycle
# Contoh cycle: A - C - D - A (balik lagi ke A = siklus)

# ==========================================================
# Spanning tree: pilih edge secukupnya buat nyambungin semua node
# tanpa bikin loop. Dengan 4 node, cukup 3 edge.
# ==========================================================
spanning_tree = [
    ('A', 'C'),   # A nyambung ke C dulu
    ('C', 'D'),   # dari C lanjut ke D
    ('D', 'B')    # dari D ke B - semua node udah nyambung semua
]
# Coba cek: dari A bisa ke C, dari C ke D, dari D ke B
# Semua 4 node terhubung, dan nggak ada loop - valid spanning tree!

# ==========================================================
# Tampilkan hasilnya
# ==========================================================
print("=" * 42)
print("  Latihan 1: Konsep Spanning Tree")
print("=" * 42)

print("\nSemua edge yang ada di graph awal:")
for i, edge in enumerate(edges, 1):
    print(f"  {i}. {edge[0]} -- {edge[1]}")

print(f"\nTotal edge di graph awal: {len(edges)}")

print("\n--- Contoh Spanning Tree yang Valid ---")
for i, edge in enumerate(spanning_tree, 1):
    print(f"  {i}. {edge[0]} -- {edge[1]}")

print(f"\nTotal edge di spanning tree: {len(spanning_tree)}")

# cek rumus: jumlah edge = jumlah node - 1
nodes = {'A', 'B', 'C', 'D'}
print(f"\nJumlah node    : {len(nodes)}")
print(f"Edge yang butuh: {len(nodes) - 1} (rumus: node - 1)")
print(f"Edge spanning tree kita: {len(spanning_tree)} ✓" if len(spanning_tree) == len(nodes) - 1 else "ada yang salah nih")


# ==========================================================
# JAWABAN ANALISIS
# ==========================================================

# 1. Apa perbedaan graph awal dan spanning tree?
#    - Graph awal punya 5 edge dan ada cycle di dalamnya.
#      Spanning tree cuma punya 3 edge dan nggak ada cycle.
#      Graph awal = "semua koneksi yang ada"
#      Spanning tree = "koneksi minimum buat nyambungin semua node"

# 2. Mengapa spanning tree tidak boleh memiliki cycle?
#    - Karena cycle itu artinya ada koneksi yang redundan (dobel/nggak perlu).
#      Bayangin masang kabel: kalau udah bisa nyambung lewat jalur A-C-D,
#      kenapa harus bikin jalur A-D lagi? mubazir
#      Spanning tree itu efisiensi - seminimal mungkin tapi semua nyambung.

# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
#    - Karena rumusnya memang N-1 (jumlah node dikurangi 1).
#      Untuk nyambungin N node tanpa cycle, harus tepat N-1 edge.
#      Lebih dari itu pasti ada cycle, kurang dari itu ada node yang terputus.
#      Di sini 4 node yang berarti butuh tepat 3 edge.
# ==========================================================
