# ==========================================================
# Nama    : Muhammad Najmi Khoiri Almunawwar
# NIM     : J0403251095
# Kelas   : TPL B
# Praktikum 12 - Materi 2: Algoritma Bellman-Ford
# ==========================================================
#
# KONSEP BELLMAN-FORD:
# Bellman-Ford adalah algoritma shortest path yang mampu menangani
# graph dengan bobot NEGATIF, berbeda dari Dijkstra.
#
# Cara kerja: "melakukan RELAKSASI seluruh edge secara berulang"
# → setiap iterasi mencoba memperbarui jarak semua node melalui semua edge
# → dilakukan sebanyak (jumlah_node - 1) kali
#
# Kenapa (n-1) kali?
# → Jalur terpendek pada graph dengan n node maksimal melewati (n-1) edge
# → Setiap iterasi menjamin setidaknya 1 node mendapat jarak finalnya

# ──────────────────────────────────────────────────────────
# Definisi Weighted Graph dengan BOBOT NEGATIF
# Ini adalah kasus yang TIDAK bisa ditangani Dijkstra
# ──────────────────────────────────────────────────────────
graph = {
    'A': {'B': 5, 'C': 4},   # A → B (bobot 5), A → C (bobot 4)
    'B': {},                   # B tidak memiliki tetangga
    'C': {'B': -2}             # C → B (bobot NEGATIF -2)
}

# Jalur ke B:
#   Langsung A → B        = 5
#   Via C:  A → C → B    = 4 + (-2) = 2   ← lebih kecil!


def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node 'start'
    ke seluruh node lain menggunakan algoritma Bellman-Ford.
    Mampu menangani bobot negatif.

    Parameter:
        graph (dict) : weighted graph dalam bentuk nested dictionary
        start (str)  : node awal pencarian

    Return:
        distances (dict) : dictionary berisi jarak terpendek
                           dari 'start' ke setiap node
    """

    # Inisialisasi semua jarak dengan tak hingga (inf)
    distances = {node: float('inf') for node in graph}

    # Jarak dari node awal ke dirinya sendiri adalah 0
    distances[start] = 0

    # Relaksasi dilakukan sebanyak (jumlah_node - 1) kali
    # Tujuan: memastikan semua kemungkinan jalur sudah dievaluasi
    for iterasi in range(len(graph) - 1):

        # Pada setiap iterasi, periksa SEMUA edge dalam graph
        for node in graph:
            for neighbor, weight in graph[node].items():

                # Kondisi relaksasi:
                # Jika jarak ke 'node' sudah diketahui (bukan inf)
                # DAN melewati 'node' memberikan jarak lebih kecil ke 'neighbor',
                # maka perbarui jarak ke 'neighbor'
                if distances[node] != float('inf') and \
                   distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    return distances


# ──────────────────────────────────────────────────────────
# Program Utama: Jalankan Bellman-Ford dari node 'A'
# ──────────────────────────────────────────────────────────
print("=" * 45)
print("  Algoritma Bellman-Ford – Shortest Path")
print("=" * 45)
print("Graph (dengan bobot negatif):")
print("  A → B (bobot  5)")
print("  A → C (bobot  4)")
print("  C → B (bobot -2)")
print()

hasil = bellman_ford(graph, 'A')

print("Jarak terpendek dari node A:")
for node, jarak in hasil.items():
    print(f"  A → {node} = {jarak}")

# ──────────────────────────────────────────────────────────
# PENJELASAN OUTPUT:
# Output: {'A': 0, 'B': 2, 'C': 4}
#
# → A ke A = 0  (titik awal)
# → A ke C = 4  (langsung A→C)
# → A ke B = 2  (via C: A→C→B = 4 + (-2) = 2, lebih kecil dari A→B = 5)
#
# TRACE LANGKAH BELLMAN-FORD (n=3, relaksasi 2 kali):
# Awal    : dist = {A:0, B:inf, C:inf}
#
# Iterasi 1 – periksa semua edge:
#   Edge A→B: dist[A]+5 = 5 < inf → dist[B] = 5
#   Edge A→C: dist[A]+4 = 4 < inf → dist[C] = 4
#   Edge C→B: dist[C]+(-2) = 4-2 = 2 < 5 → dist[B] = 2
#   Setelah iterasi 1: {A:0, B:2, C:4}
#
# Iterasi 2 – periksa semua edge lagi (tidak ada perubahan):
#   Edge A→B: 0+5=5 > 2 → tidak berubah
#   Edge A→C: 0+4=4 = 4 → tidak berubah
#   Edge C→B: 4-2=2 = 2 → tidak berubah
#   Setelah iterasi 2: {A:0, B:2, C:4}  ← FINAL
#
# MENGAPA BELLMAN-FORD BISA MENANGANI BOBOT NEGATIF?
# → Karena ia tidak langsung "mengunci" jarak seperti Dijkstra.
#   Setiap iterasi membuka kemungkinan untuk memperbarui jarak
#   yang sudah ada melalui edge berbobot negatif.
# → Dijkstra gagal karena setelah memilih A→B=5, ia langsung
#   menganggap jarak ke B sudah final dan tidak memeriksa ulang.
# ──────────────────────────────────────────────────────────
