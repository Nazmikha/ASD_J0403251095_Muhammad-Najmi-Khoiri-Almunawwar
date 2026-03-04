# ====================================================
# Nama = Muhammad Najmi Khoiri Almunawwar
# NIM = J0403251095
# Kelas = TPL B2
# ====================================================
# Latihan 1 . Memahami Kode Program (Insertion Sort)
# =====================================================

def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key

    return data


#============================================================================
# Soal
#1. Mengapa perulangan dimulai dari indeks 1?
#2. Apa fungsi variabel key?
#3. Mengapa digunakan while, bukan for?
#4. Operasi apa yang terjadi di dalam while?
#============================================================================
# Jawaban
# 1. Karena elemen pertama (indeks 0) dianggap sudah terurut dengan sendirinya
# 2. Variabel key digunakan untuk menyimpann nilai sementara yang akan disisipkan ke posisi yang benar
# 3. Digunakan while karna jumlah pergeseran yang diperlukan tidak diketahhui tepatnya, sedangkan for lebih optimal digunakan jika sudah diketahui jumlah perulangannya
# 4. Menggeser key ke j-1 dan menyisipkan key ke posisi yang benar

 
