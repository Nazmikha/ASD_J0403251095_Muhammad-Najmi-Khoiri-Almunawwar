#========IDENTITAS MAHASISWA===================
#NAMA : Muhammad Najmi Khoiri Almunawwar
#NIM  : J0403251095
#Kelas: P2
#================================================

# ==========================================================
# Latihan 7.4 - Backtracking Dasar
# Tujuan   : Memahami pola choose dan explore
# Instruksi: Membuat semua kombinasi huruf A dan B
# ==========================================================

def kombinasi(n, hasil=""):
    # ----------------------------------------------------------
    # BASE CASE: jika panjang string hasil sudah = n,
    # satu kombinasi lengkap terbentuk -> cetak dan kembali
    # ----------------------------------------------------------
    if len(hasil) == n:
        print(hasil)  # tampilkan kombinasi yang terbentuk
        return

    # ----------------------------------------------------------
    # Choose + Explore: pilih huruf 'A'
    # String hasil diperpanjang dengan 'A', lalu eksplorasi lebih dalam
    # ----------------------------------------------------------
    kombinasi(n, hasil + "A")

    # ----------------------------------------------------------
    # Choose + Explore: pilih huruf 'B'
    # String hasil diperpanjang dengan 'B', lalu eksplorasi lebih dalam
    # (Unchoose terjadi otomatis karena parameter tidak diubah permanen)
    # ----------------------------------------------------------
    kombinasi(n, hasil + "B")


# ----------------------------------------------------------
# Menjalankan fungsi kombinasi
# ----------------------------------------------------------
print("=== Latihan 4: Backtracking - Kombinasi Huruf A dan B ===")

print("Kombinasi huruf A/B dengan panjang 2:")
kombinasi(2)

print("\nKombinasi huruf A/B dengan panjang 3:")
kombinasi(3)

# ==========================================================
# DISKUSI: Bagaimana jumlah kombinasi yang dihasilkan?
#
# Jawaban:
# Jumlah kombinasi mengikuti rumus: 2^n
# karena setiap posisi memiliki 2 pilihan (A atau B).
#
# Rincian:
#   n=1: 2^1 = 2 kombinasi   -> A, B
#   n=2: 2^2 = 4 kombinasi   -> AA, AB, BA, BB
#   n=3: 2^3 = 8 kombinasi   -> AAA, AAB, ABA, ABB, BAA, BAB, BBA, BBB
#   n=4: 2^4 = 16 kombinasi
#
# Pola pohon keputusan untuk n=2:
#              start
#             /     \
#            A       B
#           / \     / \
#         AA  AB   BA  BB
#
# Program menelusuri setiap cabang dari kiri ke kanan (DFS):
# - Selalu mencoba 'A' terlebih dahulu, baru kemudian 'B'
# - Prinsip ini sama dengan Depth First Search (DFS) pada graph
# - Semakin besar n, jumlah kombinasi tumbuh secara eksponensial (2^n)
# ==========================================================
