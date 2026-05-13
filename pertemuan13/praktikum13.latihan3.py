# ==========================================================
# Nama    : Muhammad Najmi Khoiri Almunawwar
# NIM     : J0403251095
# Kelas   : TPL B
# Judul   : Praktikum 13 - Latihan 3: Implementasi Prim
# Modul   : Modul 9 - Graph III: Spanning Trees
# Matkul  : Algoritma dan Struktur Data (TPL2106)
# ==========================================================
#
# Prim itu cara berpikirnya beda dari Kruskal.
# Kalau Kruskal itu lihat semua edge dulu terus pilih yang terkecil,
# Prim itu kayak "jalan pelan-pelan" — mulai dari satu titik,
# terus cari jalan termurah ke tempat yang belum pernah didatangi.
# ==========================================================

import heapq  # heapq = priority queue, otomatis ngambil yang nilai terkecil

# graph ini undirected (dua arah), makanya tiap edge didaftarin dua kali
# misal A-C ada di graph['A'] dan juga graph['C']
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}


def prim(graph, start):
    # visited = tempat nyimpen node yang udah kita kunjungi
    # mulai dari node awal aja
    visited = set([start])

    # edges = priority queue, isinya edge-edge yang bisa kita pilih
    # dari node-node yang udah dikunjungi
    edges = []

    # masukin dulu semua tetangga dari node awal
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []
    total_weight = 0

    while edges:
        # ambil edge yang paling murah dari semua yang tersedia
        weight, u, v = heapq.heappop(edges)

        # kalau v udah dikunjungi, skip! nggak mau dobel
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight

            # dari v yang baru dikunjungi, lihat tetangga-tetangganya
            # kalau belum pernah dikunjungi, masukin ke queue
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight


# jalankan Prim dari node 'A'
mst, total = prim(graph, 'A')

print("=" * 42)
print("  Latihan 3: Prim - Hasil MST")
print("=" * 42)
print("Edge yang masuk MST:")
for u, v, w in mst:
    print(f"  {u} -- {v}  (bobot: {w})")
print(f"\nTotal bobot MST = {total}")


# ==========================================================
# JAWABAN ANALISIS
# ==========================================================

# 1. Node awal apa yang digunakan?
#    - Node 'A'. Kita bisa mulai dari node manapun sebenernya,
#      hasil MST-nya tetap sama (total bobot sama), cuma urutan
#      pemilihan edge-nya aja yang bisa beda.

# 2. Edge mana yang dipilih pertama kali?
#    - A-C dengan bobot 2. Dari node A, ada 3 pilihan:
#      ke B (4), ke C (2), ke D (5). Yang terkecil = A-C.

# 3. Bagaimana Prim menentukan edge berikutnya?
#    - Setiap kali masuk ke node baru, semua tetangga yang belum
#      dikunjungi dimasukin ke priority queue. Priority queue
#      otomatis ngurutin, jadi pas kita 'pop', yang keluar selalu
#      yang paling kecil bobotnya dari semua yang tersedia.
#      Intinya: dari posisi sekarang, pindah ke yang paling dekat/murah.

# 4. Berapa total bobot MST yang dihasilkan?
#    - Total = 2 (A-C) + 1 (C-D) + 3 (D-B) = 6
#      Sama kayak Kruskal! Karena MST itu unik (kalau bobotnya berbeda),
#      kedua algoritma akan menghasilkan total bobot yang sama.

# 5. Apa perbedaan pendekatan Prim dan Kruskal?
#    - Kruskal: "Lihat semua edge dulu, pilih yang terkecil secara global,
#      asal nggak bikin cycle." - fokusnya ke EDGE.
#
#    - Prim: "Mulai dari satu node, terus ekspansi ke tetangga terdekat
#      yang belum dikunjungi." - fokusnya ke NODE.
#
#    Kruskal cocok buat sparse graph (edge sedikit).
#    Prim lebih efisien di dense graph (banyak edge).
#    Tapi hasilnya (total bobot MST) sama-sama minimum!
# ==========================================================
