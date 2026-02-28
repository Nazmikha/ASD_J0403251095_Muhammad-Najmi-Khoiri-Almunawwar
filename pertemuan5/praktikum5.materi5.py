#========IDENTITAS MAHASISWA===================
#NAMA : Muhammad Najmi Khoiri Almunawwar
#NIM  : J0403251095
#Kelas: P2
#================================================

# ==========================================================
# Materi 6.5 - Backtracking dengan Pruning (Pemangkasan)
# Topik    : Kombinasi Biner dengan Batas Jumlah '1'
# ==========================================================
# Penjelasan Konsep:
# PRUNING adalah strategi untuk MENGHENTIKAN eksplorasi cabang
# yang sudah pasti tidak memenuhi syarat (constraint).
# Dengan pruning, pencarian menjadi lebih EFISIEN karena
# tidak semua kemungkinan perlu dieksplorasi.
#
# Contoh: kombinasi biner n=4 dengan maksimal 2 angka '1'
# Cabang yang memiliki jumlah '1' lebih dari 2 langsung dihentikan
# sehingga tidak perlu dilanjutkan ke level berikutnya.
# ==========================================================

def biner_batas(n, batas, hasil="", jumlah_1=0):
    # ----------------------------------------------------------
    # PRUNING: jika jumlah angka '1' sudah melebihi batas,
    # hentikan eksplorasi cabang ini (tidak perlu dilanjutkan)
    # ----------------------------------------------------------
    if jumlah_1 > batas:
        return  # mundur (backtrack), cabang ini tidak valid

    # ----------------------------------------------------------
    # Base case: jika panjang hasil sudah = n,
    # satu kombinasi valid telah terbentuk -> cetak
    # ----------------------------------------------------------
    if len(hasil) == n:
        print(hasil)
        return

    # ----------------------------------------------------------
    # Choose + Explore: pilih '0'
    # Jumlah '1' tidak bertambah saat memilih '0'
    # ----------------------------------------------------------
    biner_batas(n, batas, hasil + "0", jumlah_1)

    # ----------------------------------------------------------
    # Choose + Explore: pilih '1'
    # Jumlah '1' bertambah 1, sehingga diteruskan sebagai jumlah_1 + 1
    # ----------------------------------------------------------
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1)


# ----------------------------------------------------------
# Menjalankan fungsi dengan n=4 dan batas maksimal 2 angka '1'
# ----------------------------------------------------------
print("=== Materi 6.5: Backtracking dengan Pruning ===")
print("Kombinasi biner n=4, maksimal 2 angka '1':")
biner_batas(4, 2)

print("\nKombinasi biner n=3, maksimal 1 angka '1':")
biner_batas(3, 1)
