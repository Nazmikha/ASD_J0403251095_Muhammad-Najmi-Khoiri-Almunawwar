# ==========================================================
# Nama    : Muhammad Najmi Khoiri Almunawwar
# NIM     : J0403251095
# Kelas   : TPL B
# Praktikum 12 - Latihan 2: Implementasi Algoritma Dijkstra
# ==========================================================

import heapq  # digunakan untuk priority queue (min-heap)

# ──────────────────────────────────────────────────────────
# Weighted graph dengan bobot POSITIF
# Dijkstra hanya valid untuk bobot positif
# ──────────────────────────────────────────────────────────
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}


def dijkstra(graph, start):
    """
    Mencari jarak terpendek dari node 'start' ke semua node
    menggunakan algoritma Dijkstra dengan priority queue.
    Hanya valid untuk graph dengan bobot POSITIF.
    """

    # Inisialisasi: semua jarak = tak hingga, belum diketahui jaraknya
    distances = {node: float('inf') for node in graph}

    # Jarak dari start ke dirinya sendiri selalu 0
    distances[start] = 0

    # Priority queue: list of (jarak_sementara, nama_node)
    # heapq selalu mengeluarkan elemen dengan nilai TERKECIL terlebih dahulu
    priority_queue = [(0, start)]

    while priority_queue:
        # Ambil node dengan jarak terkecil dari priority queue
        current_distance, current_node = heapq.heappop(priority_queue)

        # Lewati jika jarak yang diambil sudah lebih besar dari yang tercatat
        # (artinya ada jalur lebih pendek yang sudah ditemukan sebelumnya)
        if current_distance > distances[current_node]:
            continue

        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            # Total jarak ke tetangga melalui node saat ini
            distance = current_distance + weight

            # Relaksasi: perbarui jarak jika lebih kecil dari yang tercatat
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # Masukkan ke queue dengan jarak yang sudah diperbarui
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# ──────────────────────────────────────────────────────────
# Program Utama
# ──────────────────────────────────────────────────────────
hasil = dijkstra(graph, 'A')

print("=" * 40)
print("  Latihan 2: Algoritma Dijkstra")
print("=" * 40)
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(f"  A → {node} = {distance}")


# ==========================================================
# JAWABAN ANALISIS
# ==========================================================

# 1. Berapa jarak terpendek dari A ke B?
#    → 4 (langsung A→B, tidak ada jalur alternatif yang lebih kecil ke B)

# 2. Berapa jarak terpendek dari A ke C?
#    → 2 (langsung A→C, hanya ada satu jalur)

# 3. Berapa jarak terpendek dari A ke D?
#    → 3 (melalui C: A→C→D = 2+1 = 3, lebih kecil dari A→B→D = 4+5 = 9)

# 4. Mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B?
#    → Karena total bobot A→C→D = 2+1 = 3, sedangkan A→B→D = 4+5 = 9.
#      Meskipun jumlah edge sama (2 edge), bobot setiap edge sangat berbeda.
#      Bobot A→C (2) + C→D (1) jauh lebih kecil dari A→B (4) + B→D (5).

# 5. Apa fungsi priority_queue dalam algoritma Dijkstra?
#    → Priority queue (min-heap) memastikan node dengan jarak sementara
#      TERKECIL selalu diproses lebih dahulu. Ini adalah kunci dari
#      pendekatan greedy Dijkstra: selalu ekspansi dari node termurah.
#      Tanpa priority queue, kita harus memindai semua node di setiap
#      iterasi → lebih lambat O(V²). Dengan heapq → O((V+E) log V).

# 6. Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif?
#    → Dijkstra menggunakan pendekatan greedy: begitu sebuah node diambil
#      dari priority queue, jaraknya dianggap FINAL dan tidak akan diubah.
#      Asumsi ini benar selama semua bobot positif (jarak tidak akan
#      mengecil dengan menambah lebih banyak edge).
#      Namun jika ada bobot negatif, menambah edge justru bisa memperkecil
#      total jarak. Contoh: A→B=5, A→C=4, C→B=-3 → jarak A ke B
#      sebenarnya 4+(-3)=1, tapi Dijkstra sudah "mengunci" B=5.
#      Untuk kasus ini, gunakan Bellman-Ford.
# ==========================================================
