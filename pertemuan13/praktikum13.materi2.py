# ==========================================================
# Nama    : Muhammad Najmi Khoiri Almunawwar
# NIM     : J0403251095
# Kelas   : TPL B
# Judul   : Praktikum 13 - Materi 2: Algoritma Prim
# Modul   : Modul 9 - Graph III: Spanning Trees
# Matkul  : Algoritma dan Struktur Data (TPL2106)
# ==========================================================
#
# Kalau Kruskal itu milih dari semua edge secara global,
# Prim beda — dia mulai dari SATU node terus ngebangun tree-nya
# pelan-pelan ke node-node tetangga yang paling murah.
#
# Cara kerjanya kayak gini:
#   1. Pilih satu node awal (bebas mau mulai dari mana)
#   2. Lihat semua edge yang bisa dijangkau dari node yang udah dikunjungi
#   3. Pilih yang paling murah (bobot terkecil)
#   4. Masuk ke node baru itu, lalu lihat lagi tetangga-tetangganya
#   5. Ulangi sampai semua node udah dikunjungi
#
# Analoginya: kayak kamu lagi nyebar wi-fi antar ruangan.
# Mulai dari satu ruangan, terus sambungin ke ruangan terdekat,
# dari situ sambungin lagi ke yang terdekat, dan seterusnya.
# ==========================================================

import heapq  # ini buat priority queue, supaya otomatis ngambil yang terkecil

# Graph-nya berupa dictionary bersarang (undirected = dua arah)
# Karena undirected, A-C dan C-A harus dua-duanya didaftarin
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},   # dari A bisa ke B(4), C(2), D(5)
    'B': {'A': 4, 'D': 3},             # dari B bisa ke A(4), D(3)
    'C': {'A': 2, 'D': 1},             # dari C bisa ke A(2), D(1)
    'D': {'A': 5, 'B': 3, 'C': 1}     # dari D bisa ke A(5), B(3), C(1)
}


def prim(graph, start):
    """
    Fungsi ini ngejalanin algoritma Prim mulai dari node 'start'.
    Balik dua hal: list edge MST-nya sama total bobotnya.
    """

    # visited = set node yang udah "masuk" ke MST kita
    # awalnya cuma ada node awal aja
    visited = set([start])

    # edges = priority queue berisi semua edge yang bisa dijangkau
    # dari node-node yang udah dikunjungi
    # format: (bobot, dari_node, ke_node)
    edges = []

    # masukin semua tetangga dari node awal ke priority queue
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []          # tempat nyimpen edge-edge MST
    total_weight = 0  # total biaya MST

    # selama masih ada edge yang bisa diproses...
    while edges:
        # ambil edge yang paling murah dari priority queue
        weight, u, v = heapq.heappop(edges)

        # kalau node tujuan (v) udah dikunjungi, skip aja
        # (berarti dia udah masuk MST, nggak perlu dobel)
        if v not in visited:
            visited.add(v)               # tandai v sebagai sudah dikunjungi
            mst.append((u, v, weight))   # masukkan edge ini ke MST
            total_weight += weight        # tambah bobotnya

            # sekarang dari v, lihat tetangga-tetangganya
            # kalau tetangga itu belum dikunjungi, masukin ke queue
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight


# jalankan Prim mulai dari node 'A'
mst, total = prim(graph, 'A')

print("=" * 40)
print("  Materi 2: Prim - Hasil MST")
print("=" * 40)
print("Edge yang masuk ke MST (mulai dari A):")
for edge in mst:
    u, v, w = edge
    print(f"  {u} -- {v}  (bobot: {w})")

print(f"\nTotal bobot MST = {total}")

# ==========================================================
# PENJELASAN HASIL:
#
# Mulai dari A. Masukin semua tetangga A ke queue:
#   queue = [(2,A,C), (4,A,B), (5,A,D)]
#
# Iterasi 1 - Ambil terkecil: A-C (bobot 2)
#   C belum dikunjungi - AMBIL. visited = {A, C}
#   Masukin tetangga C yang belum dikunjungi: C-D(1)
#   queue = [(1,C,D), (4,A,B), (5,A,D)]
#
# Iterasi 2 - Ambil terkecil: C-D (bobot 1)
#   D belum dikunjungi - AMBIL. visited = {A, C, D}
#   Masukin tetangga D yang belum dikunjungi: D-B(3)
#   queue = [(3,D,B), (4,A,B), (5,A,D)]
#
# Iterasi 3 - Ambil terkecil: D-B (bobot 3)
#   B belum dikunjungi - AMBIL. visited = {A, C, D, B}
#   Semua node sudah dikunjungi!
#
# MST final: A-C(2), C-D(1), D-B(3) → total = 6
#
# Hasilnya sama kayak Kruskal tapi cara berpikirnya beda.
# Kruskal: "pilih yang terkecil dari semua edge yang ada"
# Prim   : "dari posisi sekarang, pindah ke tetangga termurah"
# ==========================================================
