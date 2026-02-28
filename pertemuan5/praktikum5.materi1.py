#========IDENTITAS MAHASISWA===================
#NAMA : Muhammad Najmi Khoiri Almunawwar
#NIM  : J0403251095
#Kelas: P2
#================================================

# ==========================================================
# Materi 6.1 - Konsep Dasar Rekursif
# Topik    : Fungsi Rekursif - Menghitung Faktorial
# ==========================================================
# Penjelasan Konsep:
# Fungsi rekursif adalah fungsi yang memanggil dirinya sendiri
# untuk menyelesaikan masalah yang lebih kecil hingga
# mencapai kondisi berhenti (base case).
#
# Dua komponen utama fungsi rekursif:
# 1. BASE CASE    : kondisi berhenti agar fungsi tidak loop selamanya
# 2. RECURSIVE CASE: pemanggilan fungsi ke dirinya sendiri
#                   dengan ukuran masalah yang semakin kecil
#
# Tanpa base case -> program akan mengalami INFINITE RECURSION
# ==========================================================

def faktorial(n):
    # ----------------------------------------------------------
    # Base case: faktorial(0) = 1
    # Ketika n mencapai 0, rekursi berhenti dan mengembalikan 1
    # ----------------------------------------------------------
    if n == 0:
        return 1

    # ----------------------------------------------------------
    # Recursive case: n! = n * (n-1)!
    # Masalah diperkecil: menghitung faktorial(n-1)
    # Contoh untuk n=5:
    #   faktorial(5) = 5 * faktorial(4)
    #   faktorial(4) = 4 * faktorial(3)
    #   faktorial(3) = 3 * faktorial(2)
    #   faktorial(2) = 2 * faktorial(1)
    #   faktorial(1) = 1 * faktorial(0)
    #   faktorial(0) = 1  <-- base case tercapai
    # ----------------------------------------------------------
    return n * faktorial(n - 1)


# ----------------------------------------------------------
# Menguji fungsi faktorial
# ----------------------------------------------------------
print("=== Contoh Rekursi 1: Faktorial ===")
print("faktorial(5) =", faktorial(5))  # Output: 120
print("faktorial(3) =", faktorial(3))  # Output: 6
print("faktorial(0) =", faktorial(0))  # Output: 1
