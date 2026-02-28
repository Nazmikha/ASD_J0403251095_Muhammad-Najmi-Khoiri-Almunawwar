#========IDENTITAS MAHASISWA===================
#NAMA : Muhamamd Najmi Khoiri Almunawwar
#NIM  : J0403251095
#Kelas: P2
#================================================

# ==========================================================
# Latihan 7.3 - Rekursi pada List
# Tujuan   : Mengolah struktur data list menggunakan rekursi
# Instruksi: Mencari nilai maksimum dalam list secara rekursif
# ==========================================================

def cari_maks(data, index=0):
    # ----------------------------------------------------------
    # BASE CASE: jika index sudah berada di elemen terakhir list,
    # kembalikan elemen tersebut sebagai nilai maksimum sementara
    # ----------------------------------------------------------
    if index == len(data) - 1:
        return data[index]

    # ----------------------------------------------------------
    # RECURSIVE CASE:
    # 1. Panggil rekursif untuk mencari maks dari sisa elemen
    #    (mulai dari index + 1 hingga akhir)
    # 2. Bandingkan elemen saat ini dengan maks dari sisa elemen
    # 3. Kembalikan nilai yang lebih besar
    # ----------------------------------------------------------
    maks_sisa = cari_maks(data, index + 1)  # cari maks sisa elemen

    # Bandingkan elemen saat ini dengan maks dari sisa list
    if data[index] > maks_sisa:
        return data[index]  # elemen saat ini lebih besar
    else:
        return maks_sisa    # maks dari sisa list lebih besar


# ----------------------------------------------------------
# Menguji fungsi cari_maks
# ----------------------------------------------------------
print("=== Latihan 3: Rekursi pada List - Cari Nilai Maksimum ===")

angka = [3, 7, 2, 9, 5]
print("Data  :", angka)
print("Nilai maksimum:", cari_maks(angka))  # Output: 9

angka2 = [15, 3, 22, 8, 1]
print("\nData  :", angka2)
print("Nilai maksimum:", cari_maks(angka2))  # Output: 22

# ==========================================================
# DISKUSI & PENJELASAN ALUR PROGRAM:
#
# Contoh pemanggilan cari_maks([3, 7, 2, 9, 5]):
#
# FASE STACKING (Masuk):
#   cari_maks(data, 0) -> memanggil cari_maks(data, 1)
#   cari_maks(data, 1) -> memanggil cari_maks(data, 2)
#   cari_maks(data, 2) -> memanggil cari_maks(data, 3)
#   cari_maks(data, 3) -> memanggil cari_maks(data, 4)
#   cari_maks(data, 4) -> BASE CASE! (index = len-1 = 4), return 5
#
# FASE UNWINDING (Keluar / Perbandingan):
#   cari_maks(data, 3): data[3]=9 vs maks_sisa=5  -> return 9
#   cari_maks(data, 2): data[2]=2 vs maks_sisa=9  -> return 9
#   cari_maks(data, 1): data[1]=7 vs maks_sisa=9  -> return 9
#   cari_maks(data, 0): data[0]=3 vs maks_sisa=9  -> return 9
#
# Hasil akhir: 9 (nilai terbesar dalam list)
#
# BASE CASE   : index == len(data) - 1 -> return data[index]
#   (saat hanya tersisa 1 elemen, elemen itu adalah maks dari dirinya)
#
# RECURSIVE CASE: bandingkan data[index] vs cari_maks(data, index+1)
#   (setiap level membandingkan elemen saat ini dengan maks sisa list)
# ==========================================================
