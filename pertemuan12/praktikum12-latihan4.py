# ==========================================================
# Nama    : Muhammad Najmi Khoiri Almunawwar
# NIM     : J0403251095
# Kelas   : TPL B
# Praktikum 12 - Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus
# ==========================================================
#
# SKENARIO:
# Sebuah kampus memiliki 5 lokasi yang terhubung satu sama lain.
# Bobot pada setiap edge merepresentasikan WAKTU TEMPUH (dalam menit).
# Tujuan: mencari waktu tempuh terpendek dari Gerbang Kampus
#         ke semua lokasi lainnya menggunakan algoritma Dijkstra.
# ==========================================================

import heapq  # untuk priority queue (min-heap)

# ──────────────────────────────────────────────────────────
# Graph lokasi kampus
# Semua bobot positif → Dijkstra cocok digunakan
# ──────────────────────────────────────────────────────────
graph = {
    'Gerbang':       {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan':  {'Lab': 3},
    'Kantin':        {'Lab': 4, 'Aula': 7},
    'Lab':           {'Aula': 1},
    'Aula':          {}
}

def dijkstra(graph, start):
    """
    Mencari waktu tempuh terpendek dari lokasi 'start'
    ke semua lokasi lain menggunakan algoritma Dijkstra.

    Parameter:
        graph (dict) : graph lokasi kampus (nested dictionary)
        start (str)  : lokasi awal

    Return:
        distances (dict) : waktu tempuh minimum ke setiap lokasi
        prev (dict)      : menyimpan node sebelumnya untuk rekonstruksi jalur
    """

    # Inisialisasi semua waktu tempuh dengan tak hingga
    distances = {node: float('inf') for node in graph}

    # Simpan node sebelumnya untuk bisa merekonstruksi jalur
    prev = {node: None for node in graph}

    # Jarak dari titik awal ke dirinya sendiri = 0
    distances[start] = 0

    # Priority queue: (waktu_tempuh, nama_lokasi)
    priority_queue = [(0, start)]

    while priority_queue:
        # Ambil lokasi dengan waktu tempuh terkecil saat ini
        current_dist, current_node = heapq.heappop(priority_queue)

        # Optimasi: lewati jika jarak ini sudah tidak relevan
        if current_dist > distances[current_node]:
            continue

        # Periksa semua lokasi yang dapat dicapai dari lokasi saat ini
        for neighbor, weight in graph[current_node].items():
            # Total waktu tempuh ke tetangga melalui lokasi saat ini
            distance = current_dist + weight

            # Jika jalur ini lebih cepat, perbarui jarak dan jalur
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                prev[neighbor] = current_node  # catat dari mana datangnya
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, prev


def rekonstruksi_jalur(prev, start, tujuan):
    """
    Merekonstruksi jalur dari 'start' ke 'tujuan'
    menggunakan dictionary 'prev' yang diisi saat Dijkstra berjalan.
    """
    jalur = []
    node = tujuan
    while node is not None:
        jalur.append(node)
        node = prev[node]
    jalur.reverse()  # balik urutan karena dibangun dari tujuan ke awal
    return jalur


# ──────────────────────────────────────────────────────────
# Program Utama
# ──────────────────────────────────────────────────────────
hasil, prev = dijkstra(graph, 'Gerbang')

print("=" * 50)
print("  Latihan 4: Jalur Terpendek Lokasi Kampus")
print("=" * 50)
print("Waktu tempuh terpendek dari Gerbang Kampus:\n")

for lokasi, waktu in hasil.items():
    jalur = rekonstruksi_jalur(prev, 'Gerbang', lokasi)
    jalur_str = " → ".join(jalur)
    print(f"  {lokasi:<20} = {waktu:>2} menit  [{jalur_str}]")


# ==========================================================
# JAWABAN ANALISIS
# ==========================================================

# 1. Lokasi mana yang paling dekat dari Gerbang?
#    → Kantin, dengan waktu tempuh 2 menit (jalur langsung Gerbang→Kantin).

# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula?
#    → 7 menit, melalui jalur: Gerbang → Kantin → Lab → Aula
#      (2 + 4 + 1 = 7 menit)
#      Jalur lain yang mungkin:
#        Gerbang→Perpustakaan→Lab→Aula = 6+3+1 = 10 menit
#        Gerbang→Kantin→Aula           = 2+7   = 9 menit
#      Sehingga jalur via Kantin→Lab adalah yang terpendek.

# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan.
#    → TIDAK. Contohnya, Gerbang→Aula secara langsung lewat Kantin memakan
#      waktu 2+7=9 menit, tetapi melewati Kantin→Lab→Aula hanya 2+4+1=7 menit.
#      Juga Gerbang→Perpustakaan secara langsung = 6 menit, sementara
#      tidak ada jalur lebih pendek alternatif ke Perpustakaan.
#      Pada weighted graph, jalur terpendek ditentukan oleh TOTAL BOBOT,
#      bukan jumlah edge atau apakah ada koneksi langsung.

# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?
#    → Karena semua bobot pada graph ini POSITIF (waktu tempuh tidak mungkin
#      negatif). Dijkstra dirancang khusus untuk graph berbobot positif
#      dan bekerja sangat efisien dengan priority queue.
#      Selain itu, Dijkstra memberikan jarak terpendek ke SEMUA node
#      sekaligus dalam satu kali eksekusi, yang sangat berguna untuk
#      keperluan navigasi di lingkungan kampus.
# ==========================================================
