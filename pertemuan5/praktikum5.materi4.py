#========IDENTITAS MAHASISWA===================
#NAMA : Muhammad Najmi Khoiri Almunawwar
#NIM  : J0403251095
#Kelas: P2
#================================================

# ==========================================================
# Materi 6.4 - Konsep Dasar Backtracking
# Topik    : Kombinasi Biner menggunakan Backtracking
# ==========================================================
# Penjelasan Konsep:
# Backtracking adalah teknik pencarian solusi dengan MENCOBA
# berbagai kemungkinan. Jika suatu pilihan tidak memenuhi syarat,
# program MUNDUR (backtrack) dan mencoba pilihan lain.
#
# Pola umum backtracking:
#   Choose   -> pilih satu opsi dari kemungkinan yang ada
#   Explore  -> lanjutkan rekursi dengan pilihan tersebut
#   Unchoose -> kembali (mundur) dan coba opsi lain
#
# Pada kombinasi biner n=3, setiap posisi bisa diisi '0' atau '1'
# Sehingga total ada 2^3 = 8 kombinasi:
# 000, 001, 010, 011, 100, 101, 110, 111
# ==========================================================

def biner(n, hasil=""):
    # ----------------------------------------------------------
    # Base case: jika panjang string hasil sudah = n,
    # berarti satu kombinasi lengkap telah terbentuk -> cetak
    # ----------------------------------------------------------
    if len(hasil) == n:
        print(hasil)  # tampilkan kombinasi biner yang terbentuk
        return

    # ----------------------------------------------------------
    # Choose + Explore: pilih '0' lalu eksplorasi lebih dalam
    # String hasil diperpanjang dengan karakter '0'
    # ----------------------------------------------------------
    biner(n, hasil + "0")

    # ----------------------------------------------------------
    # Choose + Explore: pilih '1' lalu eksplorasi lebih dalam
    # String hasil diperpanjang dengan karakter '1'
    # (Unchoose terjadi otomatis karena parameter 'hasil' tidak diubah)
    # ----------------------------------------------------------
    biner(n, hasil + "1")


# ----------------------------------------------------------
# Menjalankan fungsi biner untuk menghasilkan kombinasi n=3
# ----------------------------------------------------------
print("=== Materi 6.4: Backtracking - Kombinasi Biner (n=3) ===")
print("Semua kombinasi biner 3 digit:")
biner(3) 

print("\nSemua kombinasi biner 2 digit:")
biner(2)