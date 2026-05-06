# ==========================================================
# Nama    : Muhammad Najmi Khoiri Almunawwar
# NIM     : J0403251095
# Kelas   : TPL B
# Praktikum 12 - Latihan 3: Implementasi Algoritma Bellman-Ford
# ==========================================================

# ──────────────────────────────────────────────────────────
# Weighted graph dengan bobot NEGATIF
# Kasus ini tidak bisa ditangani Dijkstra, tetapi Bellman-Ford bisa
# ──────────────────────────────────────────────────────────
graph = {
    'A': {'B': 5, 'C': 4},   # A → B bobot 5, A → C bobot 4
    'B': {},                   # B tidak punya tetangga
    'C': {'B': -2}             # C → B bobot NEGATIF -2
}

def bellman_ford(graph, start):
    """
    Mencari jarak terpendek dari node 'start' ke semua node
    menggunakan algoritma Bellman-Ford.
    Mampu menangani graph dengan bobot negatif.

    Cara kerja: relaksasi semua edge sebanyak (n-1) kali,
    di mana n = jumlah node dalam graph.
    """

    # Inisialisasi semua jarak dengan tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari node awal ke dirinya sendiri = 0
    distances[start] = 0

    # Lakukan relaksasi sebanyak (jumlah_node - 1) iterasi
    # Alasan: jalur terpendek tanpa siklus negatif maksimal melewati n-1 edge
    for _ in range(len(graph) - 1):

        # Di setiap iterasi, periksa SEMUA edge dalam graph
        for node in graph:
            for neighbor, weight in graph[node].items():

                # Hanya lakukan relaksasi jika jarak ke 'node' sudah diketahui
                # (bukan inf), agar tidak menghasilkan perhitungan yang salah
                if distances[node] != float('inf') and \
                   distances[node] + weight < distances[neighbor]:
                    # Perbarui jarak ke neighbor dengan jalur yang lebih kecil
                    distances[neighbor] = distances[node] + weight

    return distances


# ──────────────────────────────────────────────────────────
# Program Utama
# ──────────────────────────────────────────────────────────
hasil = bellman_ford(graph, 'A')

print("=" * 40)
print("  Latihan 3: Algoritma Bellman-Ford")
print("=" * 40)
print("Graph (bobot negatif):")
print("  A → B = 5")
print("  A → C = 4")
print("  C → B = -2")
print()
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(f"  A → {node} = {distance}")


# ==========================================================
# JAWABAN ANALISIS
# ==========================================================

# 1. Berapa bobot langsung dari A ke B?
#    → 5 (edge langsung A→B memiliki bobot 5)

# 2. Berapa total bobot jalur A → C → B?
#    → A→C = 4, C→B = -2 → Total = 4 + (-2) = 2

# 3. Jalur mana yang menghasilkan jarak lebih kecil menuju B?
#    → Jalur A → C → B dengan total bobot 2,
#      lebih kecil dari jalur langsung A → B = 5.
#      Meskipun melewati lebih banyak edge, adanya bobot negatif di C→B
#      membuat total jalur menjadi lebih kecil.

# 4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif?
#    → Karena Bellman-Ford tidak langsung "mengunci" jarak sebuah node
#      seperti Dijkstra. Setiap iterasi memeriksa ulang SEMUA edge dan
#      memperbarui jarak jika ditemukan jalur yang lebih kecil, termasuk
#      jalur yang memanfaatkan edge berbobot negatif.
#      Proses ini diulang (n-1) kali sehingga semua kemungkinan jalur
#      dievaluasi dan hasil akhirnya akurat.

# 5. Apa yang dimaksud dengan proses relaksasi edge?
#    → Relaksasi adalah proses memeriksa apakah jarak ke suatu node
#      dapat diperkecil dengan melewati node lain.
#      Formula relaksasi: if dist[u] + w(u,v) < dist[v] → update dist[v]
#      Artinya: "apakah melewati u lebih murah dari yang sudah tercatat di v?"
#      Bellman-Ford melakukan ini untuk SEMUA edge di setiap iterasi.

# 6. Apa perbedaan utama Bellman-Ford dan Dijkstra?
#    → Dijkstra (Greedy):
#         - Memilih node dengan jarak terkecil terlebih dahulu (priority queue)
#         - Jarak node yang sudah diproses dianggap FINAL
#         - Tidak bisa menangani bobot negatif
#         - Lebih cepat: O((V+E) log V)
#
#    → Bellman-Ford (Relaksasi berulang):
#         - Memeriksa semua edge di setiap iterasi (n-1 kali)
#         - Jarak bisa diperbarui berkali-kali selama proses
#         - Mampu menangani bobot negatif
#         - Lebih lambat: O(V × E)
#
#    Pilih Dijkstra jika semua bobot positif (lebih cepat).
#    Pilih Bellman-Ford jika ada kemungkinan bobot negatif.
# ==========================================================
