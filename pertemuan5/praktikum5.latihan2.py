#========IDENTITAS MAHASISWA===================
#NAMA : Muhammad Najmi Khoiri Almunawwar
#NIM  : J0403251095
#Kelas: P2
#================================================

# ==========================================================
# Latihan 7.2 - Tracing Rekursi
# Tujuan   : Memahami alur masuk (stacking) dan keluar (unwinding)
# ==========================================================

def countdown(n):
    # ----------------------------------------------------------
    # BASE CASE: ketika n = 0, rekursi berhenti
    # Ini adalah titik paling dalam dari call stack
    # ----------------------------------------------------------
    if n == 0:
        print("Selesai")  # tanda bahwa base case telah tercapai
        return

    # ----------------------------------------------------------
    # FASE STACKING: print "Masuk" sebelum pemanggilan rekursif
    # Baris ini dieksekusi saat fungsi MASUK ke call stack
    # Urutan output: 3, 2, 1 (dari besar ke kecil)
    # ----------------------------------------------------------
    print("Masuk:", n)

    # ----------------------------------------------------------
    # Pemanggilan rekursif dengan n dikurangi 1
    # Fungsi ini "menunggu" sampai countdown(n-1) selesai
    # ----------------------------------------------------------
    countdown(n - 1)

    # ----------------------------------------------------------
    # FASE UNWINDING: print "Keluar" setelah pemanggilan rekursif selesai
    # Baris ini dieksekusi saat fungsi KELUAR dari call stack
    # Urutan output: 1, 2, 3 (dari kecil ke besar / TERBALIK)
    # ----------------------------------------------------------
    print("Keluar:", n)


# ----------------------------------------------------------
# Menjalankan fungsi countdown
# ----------------------------------------------------------
print("=== Latihan 2: Tracing Rekursi ===")
countdown(3)

# ==========================================================
# DISKUSI: Mengapa output 'Keluar' muncul TERBALIK?
#
# Jawaban:
# Output "Keluar" muncul terbalik karena mengikuti prinsip
# LIFO (Last In First Out) dari call stack, sama seperti Stack.
#
# Saat rekursi berjalan:
# - countdown(3) memanggil countdown(2) -> MENUNGGU
# - countdown(2) memanggil countdown(1) -> MENUNGGU
# - countdown(1) memanggil countdown(0) -> MENUNGGU
# - countdown(0) = base case -> print "Selesai" -> SELESAI
#
# Setelah base case, fungsi kembali satu per satu (unwinding):
# - countdown(1) lanjut setelah countdown(0) selesai -> print "Keluar: 1"
# - countdown(2) lanjut setelah countdown(1) selesai -> print "Keluar: 2"
# - countdown(3) lanjut setelah countdown(2) selesai -> print "Keluar: 3"
#
# Karena yang masuk TERAKHIR (countdown(1)) keluar PERTAMA,
# maka urutan "Keluar" adalah 1, 2, 3 (kebalikan dari "Masuk" 3, 2, 1)
#
# Output lengkap program:
# Masuk: 3
# Masuk: 2
# Masuk: 1
# Selesai
# Keluar: 1
# Keluar: 2
# Keluar: 3
# ==========================================================
