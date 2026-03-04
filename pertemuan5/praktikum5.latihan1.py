#========IDENTITAS MAHASISWA===================
#NAMA : Muhammad Najmi Khoiri Almunawwar
#NIM  : J0403251095
#Kelas: P2
#=============================================
# ==========================================================
# Latihan 7.1 - Rekursi Dasar: Menghitung Nilai Pangkat
# Tujuan   : Memahami base case dan recursive case
# ==========================================================

def pangkat(a, n):
    # ----------------------------------------------------------
    # BASE CASE: a^0 = 1 untuk semua nilai a
    # Ketika pangkat (n) mencapai 0, rekursi berhenti
    # dan mengembalikan nilai 1
    # ----------------------------------------------------------
    if n == 0:
        return 1

    # ----------------------------------------------------------
    # RECURSIVE CASE: a^n = a * a^(n-1)
    # Masalah diperkecil: menghitung pangkat(a, n-1)
    # ----------------------------------------------------------
    return a * pangkat(a, n - 1)


# ----------------------------------------------------------
# Menguji fungsi pangkat
# ----------------------------------------------------------
print("=== Latihan 1: Rekursi Pangkat ===")
print("pangkat(2, 4) =", pangkat(2, 4))  # Output: 16
print("pangkat(3, 3) =", pangkat(3, 3))  # Output: 27
print("pangkat(5, 0) =", pangkat(5, 0))  # Output: 1

# ==========================================================
# DISKUSI & PENJELASAN ALUR PROGRAM:
#
# Contoh pemanggilan pangkat(2, 4):
#
# FASE STACKING (Masuk / Pemanggilan):
#   pangkat(2, 4) -> menunggu pangkat(2, 3)
#   pangkat(2, 3) -> menunggu pangkat(2, 2)
#   pangkat(2, 2) -> menunggu pangkat(2, 1)
#   pangkat(2, 1) -> menunggu pangkat(2, 0)
#   pangkat(2, 0) -> BASE CASE! mengembalikan 1
#
# FASE UNWINDING (Keluar / Pengembalian):
#   pangkat(2, 0) = 1
#   pangkat(2, 1) = 2 * 1    = 2
#   pangkat(2, 2) = 2 * 2    = 4
#   pangkat(2, 3) = 2 * 4    = 8
#   pangkat(2, 4) = 2 * 8    = 16  <- hasil akhir
#
# BASE CASE   : if n == 0 -> return 1
#   (setiap angka dipangkatkan 0 hasilnya selalu 1)
#
# RECURSIVE CASE: return a * pangkat(a, n - 1)
#   (pangkat dikurangi 1 setiap pemanggilan hingga mencapai 0)
# ==========================================================
