#========IDENTITAS MAHASISWA===================
#NAMA : Muhammad Najmi Khoiri Almunawwar
#NIM  : J0403251095
#Kelas: P2
#================================================

# ==========================================================
# Materi 6.2 - Tracing Rekursi (Call Stack)
# Topik    : Memahami alur Masuk (Stacking) dan Keluar (Unwinding)
# ==========================================================
# Penjelasan Konsep:
# Saat fungsi rekursif dipanggil, setiap pemanggilan ditumpuk
# di dalam call stack (seperti tumpukan piring).
#
# Fase STACKING (Masuk):
#   - Fungsi memanggil dirinya sendiri
#   - Call stack terus bertambah ke atas
#   - Contoh: hitung(3) -> hitung(2) -> hitung(1) -> hitung(0)
#
# Fase UNWINDING (Keluar):
#   - Setelah base case tercapai, fungsi kembali satu per satu
#   - Call stack mengurai dari atas ke bawah
#   - Contoh: hitung(0) selesai -> hitung(1) selesai -> dst
# ==========================================================

def hitung(n):
    # ----------------------------------------------------------
    # Base case: berhenti ketika n = 0
    # Ini adalah titik paling dalam dari rekursi
    # ----------------------------------------------------------
    if n == 0:
        print("Selesai")  # tanda bahwa base case tercapai
        return

    # ----------------------------------------------------------
    # Fase STACKING: dicetak sebelum pemanggilan rekursif
    # Artinya: fungsi ini belum selesai, masih menunggu
    # ----------------------------------------------------------
    print("Masuk:", n)   # fase stacking - fungsi masuk ke call stack

    hitung(n - 1)        # pemanggilan rekursif dengan n diperkecil

    # ----------------------------------------------------------
    # Fase UNWINDING: dicetak setelah pemanggilan rekursif selesai
    # Artinya: fungsi yang lebih dalam sudah selesai, kini giliran ini
    # Output "Keluar" akan muncul terbalik karena LIFO (Last In First Out)
    # ----------------------------------------------------------
    print("Keluar:", n)  # fase unwinding - fungsi keluar dari call stack


# ----------------------------------------------------------
# Menjalankan fungsi dan mengamati urutan output
# ----------------------------------------------------------
print("=== Materi 6.2: Tracing Rekursi (Call Stack) ===")
hitung(3)

# ----------------------------------------------------------
# Penjelasan urutan output yang dihasilkan:
#
# Masuk: 3    <- hitung(3) dipanggil, menunggu hitung(2)
# Masuk: 2    <- hitung(2) dipanggil, menunggu hitung(1)
# Masuk: 1    <- hitung(1) dipanggil, menunggu hitung(0)
# Selesai     <- hitung(0) = base case, kembali ke hitung(1)
# Keluar: 1   <- hitung(1) selesai, kembali ke hitung(2)
# Keluar: 2   <- hitung(2) selesai, kembali ke hitung(3)
# Keluar: 3   <- hitung(3) selesai
# ----------------------------------------------------------
