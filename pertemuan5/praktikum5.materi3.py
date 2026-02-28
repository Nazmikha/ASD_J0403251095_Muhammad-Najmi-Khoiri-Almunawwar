#========IDENTITAS MAHASISWA===================
#NAMA : Muhammad Najmi Khoiri Almunawwar
#NIM  : J0403251095
#Kelas: P2
#================================================

# ==========================================================
# Materi 6.3 - Rekursi pada Data List
# Topik    : Menjumlahkan elemen list secara rekursif
# ==========================================================
# Penjelasan Konsep:
# Rekursi dapat digunakan untuk memproses data list secara
# bertahap dengan menggeser indeks (index) dari 0 hingga akhir list.
#
# Cara kerja:
# - Setiap pemanggilan rekursif memproses SATU elemen (index saat ini)
# - Kemudian memanggil dirinya lagi dengan index + 1
# - Berhenti saat index sudah melewati semua elemen list
#
# Contoh untuk [2, 4, 6, 8]:
#   jumlah_list([2,4,6,8], 0) = 2 + jumlah_list([2,4,6,8], 1)
#   jumlah_list([2,4,6,8], 1) = 4 + jumlah_list([2,4,6,8], 2)
#   jumlah_list([2,4,6,8], 2) = 6 + jumlah_list([2,4,6,8], 3)
#   jumlah_list([2,4,6,8], 3) = 8 + jumlah_list([2,4,6,8], 4)
#   jumlah_list([2,4,6,8], 4) = 0  <- base case (index == len(data))
#   Hasil akhir: 2 + 4 + 6 + 8 + 0 = 20
# ==========================================================

def jumlah_list(data, index=0):
    # ----------------------------------------------------------
    # Base case: jika index sudah mencapai panjang list,
    # tidak ada elemen tersisa, kembalikan 0
    # ----------------------------------------------------------
    if index == len(data):
        return 0

    # ----------------------------------------------------------
    # Recursive case:
    # Ambil elemen pada posisi index saat ini,
    # lalu tambahkan dengan hasil penjumlahan sisa elemen berikutnya
    # ----------------------------------------------------------
    return data[index] + jumlah_list(data, index + 1)


# ----------------------------------------------------------
# Menguji fungsi jumlah_list dengan berbagai data
# ----------------------------------------------------------
print("=== Materi 6.3: Rekursi pada Data List ===")

angka1 = [2, 4, 6, 8]
print("Data  :", angka1)
print("Jumlah:", jumlah_list(angka1))  # Output: 20

angka2 = [1, 2, 3, 4, 5]
print("\nData  :", angka2)
print("Jumlah:", jumlah_list(angka2))  # Output: 15

angka3 = [10, 20, 30]
print("\nData  :", angka3)
print("Jumlah:", jumlah_list(angka3))  # Output: 60
