# ==========================================================
# Nama    : Muhammad Najmi Khoiri Almunawwar
# NIM     : J0403251095
# Kelas   : TPL B
# Judul   : Praktikum 13 - Materi 1: Algoritma Kruskal
# Modul   : Modul 9 - Graph III: Spanning Trees
# Matkul  : Algoritma dan Struktur Data (TPL2106)
# ==========================================================
#
# Oke jadi gini, Kruskal itu cara kerja-nya simpel banget:
# - Kumpulkan semua edge yang ada
# - Urutin dari yang paling murah (bobot terkecil) ke yang paling mahal
# - Ambil satu-satu, tapi SKIP kalau bakal bikin siklus (cycle)
# - Berhenti kalau semua node udah nyambung
#
# Analogi gampangnya: bayangin kamu mau masang kabel ke semua gedung
# dengan budget seminim mungkin. Kamu bakal milih jalur kabel yang murah
# dulu, tapi kamu nggak mau bikin kabel yang muter-muter (cycle) karena
# itu buang-buang biaya aja.
# ==========================================================

# Daftar edge: formatnya (bobot, node1, node2)
# ini semua jalur yang ADA di graph, belum tentu semua dipakai
edges = [
    (1, 'C', 'D'),   # C ke D cuma 1, ini yang paling murah
    (2, 'A', 'C'),   # A ke C bobotnya 2
    (3, 'B', 'D'),   # B ke D bobotnya 3
    (4, 'A', 'B'),   # A ke B bobotnya 4
    (5, 'A', 'D')    # A ke D bobotnya 5, ini yang paling mahal
]

# Step 1: urutin semua edge dari bobot terkecil ke terbesar
# Python bisa sort tuple otomatis berdasarkan elemen pertama (bobot)
edges.sort()

mst = []          # ini tempat nyimpen edge-edge yang masuk MST
total_weight = 0  # akumulasi total bobot MST

# connected = set node-node yang sudah "masuk" ke MST kita
# awalnya kosong, nanti diisi satu-satu
connected = set()

# sekarang kita loop semua edge yang udah diurutin tadi
for weight, u, v in edges:

    # cek: apakah edge ini aman? (nggak bikin cycle)
    # logika sederhananya: kalau salah satu ujung node belum masuk
    # ke 'connected', berarti kita aman untuk nambah edge ini
    # karena nggak mungkin bikin siklus kalau salah satu node-nya baru
    if u not in connected or v not in connected:
        mst.append((u, v, weight))   # masukin ke MST
        total_weight += weight        # tambah bobotnya ke total

        # tandai kedua node ini sebagai sudah terhubung
        connected.add(u)
        connected.add(v)

# tampilkan hasilnya
print("=" * 40)
print("  Materi 1: Kruskal - Hasil MST")
print("=" * 40)
print("Edge yang masuk ke MST:")
for edge in mst:
    u, v, w = edge
    print(f"  {u} -- {v}  (bobot: {w})")

print(f"\nTotal bobot MST = {total_weight}")

# ==========================================================
# PENJELASAN HASIL:
#
# Urutan edge setelah di-sort: C-D(1), A-C(2), B-D(3), A-B(4), A-D(5)
#
# Proses pemilihan satu-satu:
#   C-D (bobot 1) - C dan D belum ada di connected → AMBIL 
#                   connected = {C, D}
#
#   A-C (bobot 2)- A belum ada di connected → AMBIL 
#                   connected = {C, D, A}
#
#   B-D (bobot 3) - B belum ada di connected → AMBIL 
#                   connected = {C, D, A, B}
#
#   A-B (bobot 4) - A dan B udah dua-duanya di connected → SKIP
#                   (kalau diambil bakal bentuk cycle A-C-D-B-A)
#
#   A-D (bobot 5) - A dan D udah di connected → SKIP juga
#
# Hasil akhir MST: C-D, A-C, B-D  →  total = 1+2+3 = 6
#
# Catatan: Versi Kruskal di sini pakai pengecekan cycle yang simpel.
# Untuk graph yang lebih kompleks, idealnya pakai Union-Find / Disjoint Set
# supaya pengecekan cycle-nya lebih akurat dan nggak salah.
# ==========================================================
