# ==========================================================
# Nama    : Muhammad Najmi Khoiri Almunawwar
# NIM     : J0403251095
# Kelas   : TPL B
# Praktikum 12 - Latihan 5: Studi Kasus Shortest Path Antar Kota
# ==========================================================
#
# SKENARIO:
# Terdapat 4 kota yang terhubung oleh jalan dengan jarak (bobot) tertentu.
# Tujuan: mencari jarak terpendek dari kota Bogor ke semua kota lainnya.
#
# Koneksi antar kota:
#   Bogor  → Jakarta  = 5
#   Bogor  → Depok    = 2
#   Depok  → Jakarta  = 2
#   Jakarta → Bandung  = 7
#   Depok  → Bandung  = 6
# ==========================================================

import heapq  # dibutuhkan untuk priority queue (min-heap)

# ──────────────────────────────────────────────────────────
# Representasi weighted graph antar kota menggunakan nested dictionary
# Format: graph[kota_asal][kota_tujuan] = jarak_km
# ──────────────────────────────────────────────────────────
graph = {
    'Bogor':   {'Jakarta': 5, 'Depok': 2},   # Bogor terhubung ke Jakarta & Depok
    'Depok':   {'Jakarta': 2, 'Bandung': 6},  # Depok terhubung ke Jakarta & Bandung
    'Jakarta': {'Bandung': 7},                 # Jakarta terhubung ke Bandung
    'Bandung': {}                              # Bandung tidak punya edge keluar
}

# Kemungkinan jalur dari Bogor ke Bandung:
#   1. Bogor → Jakarta → Bandung      = 5 + 7 = 12
#   2. Bogor → Depok  → Jakarta → Bandung = 2 + 2 + 7 = 11
#   3. Bogor → Depok  → Bandung       = 2 + 6 = 8   ← terpendek!


def dijkstra(graph, start):
    """
    Mencari jarak terpendek dari kota 'start' ke semua kota lain
    menggunakan algoritma Dijkstra.

    Algoritma Dijkstra bekerja dengan prinsip greedy:
    selalu memproses kota dengan jarak sementara TERKECIL lebih dahulu,
    menggunakan priority queue (min-heap) untuk efisiensi.

    Parameter:
        graph (dict) : weighted graph antar kota
        start (str)  : nama kota awal

    Return:
        distances (dict) : jarak terpendek dari 'start' ke tiap kota
        prev (dict)      : kota sebelumnya untuk rekonstruksi jalur
    """

    # Langkah 1: Inisialisasi semua jarak = tak hingga (belum diketahui)
    distances = {node: float('inf') for node in graph}

    # Menyimpan kota sebelumnya untuk rekonstruksi rute perjalanan
    prev = {node: None for node in graph}

    # Langkah 2: Jarak kota asal ke dirinya sendiri = 0
    distances[start] = 0

    # Langkah 3: Masukkan kota awal ke priority queue
    # Format elemen: (jarak_sementara, nama_kota)
    priority_queue = [(0, start)]

    # Langkah 4: Proses selama masih ada kota di priority queue
    while priority_queue:

        # Ambil kota dengan jarak terkecil saat ini
        current_dist, current_city = heapq.heappop(priority_queue)

        # Lewati jika entri ini sudah usang (ada jalur lebih pendek ditemukan)
        if current_dist > distances[current_city]:
            continue

        # Langkah 5: Periksa semua kota tetangga yang bisa dicapai
        for neighbor, weight in graph[current_city].items():
            # Hitung total jarak ke tetangga melalui kota saat ini
            new_dist = current_dist + weight

            # Langkah 6: Relaksasi - perbarui jarak jika lebih kecil
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                prev[neighbor] = current_city   # catat rute
                heapq.heappush(priority_queue, (new_dist, neighbor))

    return distances, prev


def rekonstruksi_rute(prev, start, tujuan):
    """
    Merekonstruksi rute perjalanan dari kota 'start' ke 'tujuan'
    berdasarkan dictionary 'prev' yang diisi saat Dijkstra berjalan.
    """
    rute = []
    kota = tujuan
    # Telusuri dari tujuan kembali ke awal menggunakan pointer 'prev'
    while kota is not None:
        rute.append(kota)
        kota = prev[kota]
    rute.reverse()  # balik urutan agar dari awal ke tujuan
    return rute


# ──────────────────────────────────────────────────────────
# Program Utama: Jalankan Dijkstra dari Bogor
# ──────────────────────────────────────────────────────────
NODE_AWAL = 'Bogor'   # node awal yang ditentukan

hasil, prev = dijkstra(graph, NODE_AWAL)

print("=" * 55)
print("  Latihan 5: Shortest Path Antar Kota (Dijkstra)")
print("=" * 55)
print(f"Node awal: {NODE_AWAL}\n")
print(f"{'Tujuan':<12} {'Jarak':>6}   Rute Perjalanan")
print("-" * 55)

for kota, jarak in hasil.items():
    rute = rekonstruksi_rute(prev, NODE_AWAL, kota)
    rute_str = " → ".join(rute)
    print(f"  {kota:<12} = {jarak:>3}      {rute_str}")

print()

# Ringkasan
min_kota = min((k for k in hasil if k != NODE_AWAL), key=lambda k: hasil[k])
max_kota = max((k for k in hasil if k != NODE_AWAL), key=lambda k: hasil[k])
print(f"Kota terdekat dari {NODE_AWAL}: {min_kota} ({hasil[min_kota]} km)")
print(f"Kota terjauh  dari {NODE_AWAL}: {max_kota} ({hasil[max_kota]} km)")


# ==========================================================
# JAWABAN ANALISIS
# ==========================================================

# 1. Node awal yang digunakan apa?
#    → Bogor (variabel NODE_AWAL = 'Bogor')

# 2. Node mana yang memiliki jarak paling kecil dari node awal?
#    → Depok, dengan jarak 2 (jalur langsung Bogor→Depok = 2)

# 3. Node mana yang memiliki jarak paling besar dari node awal?
#    → Bandung, dengan jarak 8 (jalur Bogor→Depok→Bandung = 2+6 = 8)
#      Lebih kecil dari Bogor→Jakarta→Bandung = 5+7=12
#      dan Bogor→Depok→Jakarta→Bandung = 2+2+7=11

# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus ini:
#    → Langkah-langkah Dijkstra pada kasus ini:
#
#    INISIALISASI:
#      dist = {Bogor:0, Depok:inf, Jakarta:inf, Bandung:inf}
#      queue = [(0, Bogor)]
#
#    ITERASI 1 – Proses Bogor (dist=0):
#      → Update Depok:   0+2=2   < inf → dist[Depok]   = 2
#      → Update Jakarta: 0+5=5   < inf → dist[Jakarta] = 5
#      queue = [(2,Depok), (5,Jakarta)]
#
#    ITERASI 2 – Proses Depok (dist=2):
#      → Cek Jakarta:  2+2=4 < 5   → dist[Jakarta] = 4
#      → Cek Bandung:  2+6=8 < inf → dist[Bandung] = 8
#      queue = [(4,Jakarta), (5,Jakarta_lama), (8,Bandung)]
#
#    ITERASI 3 – Proses Jakarta (dist=4):
#      → Cek Bandung: 4+7=11 > 8  → tidak diperbarui
#      queue = [(5,Jakarta_lama), (8,Bandung)]
#
#    ITERASI 4 – Proses Jakarta_lama (dist=5): DILEWATI (5 > 4)
#
#    ITERASI 5 – Proses Bandung (dist=8): tidak ada tetangga
#
#    HASIL FINAL:
#      Bogor   = 0
#      Depok   = 2   (Bogor→Depok)
#      Jakarta = 4   (Bogor→Depok→Jakarta)
#      Bandung = 8   (Bogor→Depok→Bandung)
# ==========================================================
