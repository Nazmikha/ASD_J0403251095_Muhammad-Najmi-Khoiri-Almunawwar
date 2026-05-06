# ==========================================================
# Nama    : Muhammad Najmi Khoiri Almunawwar
# NIM     : J0403251095
# Kelas   : TPL B
# Praktikum 12 - Materi 1: Algoritma Dijkstra
# ==========================================================
#
# KONSEP DIJKSTRA:
# Algoritma Dijkstra mencari jarak terpendek dari satu node sumber
# ke semua node lain pada weighted graph dengan bobot POSITIF.
# Prinsip kerja: "Selalu pilih node dengan jarak sementara paling kecil"
# → disebut pendekatan GREEDY.
#
# Langkah umum:
#   1. Set jarak node awal = 0, node lain = tak hingga (inf)
#   2. Masukkan node awal ke priority queue
#   3. Ambil node dengan jarak terkecil dari queue
#   4. Perbarui jarak semua tetangganya jika ditemukan jalur lebih pendek
#   5. Ulangi hingga queue kosong
# ==========================================================

import heapq  # modul bawaan Python untuk priority queue (min-heap)

# ──────────────────────────────────────────────────────────
# Definisi Weighted Graph (graph berbobot)
# Representasi: nested dictionary (dictionary bersarang)
# Format: graph[node_asal][node_tujuan] = bobot_edge
# ──────────────────────────────────────────────────────────
graph = {
    'A': {'B': 4, 'C': 2},   # A → B (bobot 4), A → C (bobot 2)
    'B': {'D': 5},             # B → D (bobot 5)
    'C': {'D': 1},             # C → D (bobot 1)
    'D': {}                    # D tidak punya tetangga (node tujuan akhir)
}

def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node 'start'
    ke seluruh node lain menggunakan algoritma Dijkstra.

    Parameter:
        graph (dict) : weighted graph dalam bentuk nested dictionary
        start (str)  : node awal pencarian

    Return:
        distances (dict) : dictionary berisi jarak terpendek
                           dari 'start' ke setiap node
    """

    # Inisialisasi semua jarak dengan tak hingga (belum diketahui)
    distances = {node: float('inf') for node in graph}

    # Jarak dari node awal ke dirinya sendiri adalah 0
    distances[start] = 0

    # Priority queue menyimpan tuple (jarak_sementara, nama_node)
    # heapq Python adalah MIN-heap → node dengan jarak terkecil selalu diambil lebih dulu
    priority_queue = [(0, start)]

    while priority_queue:
        # Ambil node dengan jarak terkecil saat ini dari priority queue
        current_distance, current_node = heapq.heappop(priority_queue)

        # Optimasi: jika jarak yang tercatat sudah lebih kecil dari jarak
        # yang baru diambil, berarti node ini sudah diproses → lewati
        if current_distance > distances[current_node]:
            continue

        # Periksa semua tetangga (neighbor) dari node saat ini
        for neighbor, weight in graph[current_node].items():
            # Hitung total jarak jika melewati current_node menuju neighbor
            distance = current_distance + weight

            # Relaksasi: jika jarak baru lebih kecil dari yang sudah tercatat,
            # perbarui jarak dan masukkan ke priority queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# ──────────────────────────────────────────────────────────
# Program Utama: Jalankan Dijkstra dari node 'A'
# ──────────────────────────────────────────────────────────
print("=" * 45)
print("  Algoritma Dijkstra – Shortest Path")
print("=" * 45)
print("Graph:")
print("  A → B (bobot 4)")
print("  A → C (bobot 2)")
print("  B → D (bobot 5)")
print("  C → D (bobot 1)")
print()

hasil = dijkstra(graph, 'A')

print("Jarak terpendek dari node A:")
for node, jarak in hasil.items():
    print(f"  A → {node} = {jarak}")

# ──────────────────────────────────────────────────────────
# PENJELASAN OUTPUT:
# Output: {'A': 0, 'B': 4, 'C': 2, 'D': 3}
#
# → A ke A = 0  (titik awal)
# → A ke B = 4  (langsung A→B, karena tidak ada jalur alternatif lebih pendek)
# → A ke C = 2  (langsung A→C)
# → A ke D = 3  (via C: A→C→D = 2+1 = 3, lebih kecil dari A→B→D = 4+5 = 9)
#
# TRACE LANGKAH DIJKSTRA:
# Iterasi 1: Ambil A (dist=0) → update B=4, C=2  → queue: [(2,C),(4,B)]
# Iterasi 2: Ambil C (dist=2) → update D=2+1=3   → queue: [(3,D),(4,B)]
# Iterasi 3: Ambil D (dist=3) → tidak ada tetangga → queue: [(4,B)]
# Iterasi 4: Ambil B (dist=4) → coba D: 4+5=9 > 3 → tidak diupdate
# Selesai. Hasil final: A=0, B=4, C=2, D=3
# ──────────────────────────────────────────────────────────
