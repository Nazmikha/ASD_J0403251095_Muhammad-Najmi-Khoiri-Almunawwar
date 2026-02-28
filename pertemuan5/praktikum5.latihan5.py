#========IDENTITAS MAHASISWA===================
#NAMA : Muhammad Najmi Khoiri Almunawwar
#NIM  : J0403251095
#Kelas: P2
#================================================

# ==========================================================
# Latihan 7.5 - Studi Kasus: Generator PIN
# Tujuan   : Menghasilkan semua kemungkinan PIN 3 digit
#            menggunakan angka 0 sampai 2 dengan backtracking
# ==========================================================

def buat_pin(panjang, hasil=""):
    # ----------------------------------------------------------
    # BASE CASE: jika panjang string hasil sudah = panjang yang diinginkan,
    # satu PIN lengkap telah terbentuk -> cetak dan kembali
    # ----------------------------------------------------------
    if len(hasil) == panjang:
        print("PIN:", hasil)  # tampilkan PIN yang terbentuk
        return

    # ----------------------------------------------------------
    # EXPLORE: coba setiap angka yang mungkin (0, 1, 2)
    # Untuk setiap angka, lakukan Choose + Explore:
    #   - Tambahkan angka ke string hasil
    #   - Panggil rekursif untuk melengkapi digit berikutnya
    # Unchoose terjadi otomatis setelah rekursi kembali
    # ----------------------------------------------------------
    for angka in ["0", "1", "2"]:
        # Choose: pilih angka saat ini
        # Explore: eksplorasi lebih dalam dengan angka ditambahkan
        buat_pin(panjang, hasil + angka)


# ----------------------------------------------------------
# Menjalankan generator PIN 3 digit
# ----------------------------------------------------------
print("=== Latihan 5: Studi Kasus - Generator PIN ===")
print("Semua kemungkinan PIN 3 digit (angka 0-2):")
buat_pin(3)

# Menghitung total PIN yang dihasilkan
total = 3 ** 3  # 3 pilihan angka, 3 posisi digit
print(f"\nTotal PIN yang dihasilkan: {total}")

# ==========================================================
# DISKUSI: Bagaimana cara mencegah angka yang sama muncul berulang?
#
# Jawaban:
# Untuk mencegah angka yang sama muncul berulang dalam satu PIN,
# kita perlu menambahkan PRUNING: hanya pilih angka yang belum
# ada di dalam string 'hasil'.
#
# Solusinya adalah mengecek apakah angka sudah ada di 'hasil'
# sebelum menambahkannya (teknik ini menghasilkan PERMUTASI):
# ==========================================================

print("\n--- BONUS: Generator PIN tanpa angka berulang ---")

def buat_pin_unik(panjang, hasil=""):
    # ----------------------------------------------------------
    # BASE CASE: PIN lengkap terbentuk -> cetak
    # ----------------------------------------------------------
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return

    for angka in ["0", "1", "2"]:
        # ----------------------------------------------------------
        # PRUNING: hanya lanjutkan jika angka belum ada di hasil
        # Ini mencegah angka yang sama muncul berulang dalam satu PIN
        # ----------------------------------------------------------
        if angka not in hasil:
            buat_pin_unik(panjang, hasil + angka)

print("Semua PIN 3 digit tanpa pengulangan angka:")
buat_pin_unik(3)

total_unik = 3 * 2 * 1  # permutasi: 3! = 6
print(f"\nTotal PIN unik yang dihasilkan: {total_unik}")

# ==========================================================
# Perbandingan:
# - Dengan pengulangan (buat_pin)    : 3^3 = 27 kemungkinan
# - Tanpa pengulangan (buat_pin_unik): 3!  =  6 kemungkinan (permutasi)
#
# Kunci perbedaannya ada pada kondisi: if angka not in hasil
# yang berfungsi sebagai PRUNING untuk memangkas cabang
# yang mengandung angka duplikat.
# ==========================================================
