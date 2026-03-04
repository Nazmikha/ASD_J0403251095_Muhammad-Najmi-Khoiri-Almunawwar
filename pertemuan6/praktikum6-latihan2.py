# ====================================================
# Nama = Muhammad Najmi Khoiri Almunawwar
# NIM = J0403251095
# Kelas = TPL B2
# ====================================================
# Latihan  2 . Melengkapi Potongan Kod
# =====================================================

 
# def insertion_sort(data):
# for i in range(1, len(data)):
#  key = data[i]
#  j = i - 1
# 
#  while j >= 0 and ______________________:
#  data[j + 1] = data[j]
#  j -= 1

#  ______________________

#  return data

#==========================================================
#Soal:
# 1. Lengkapi kondisi agar menjadi sorting ascending.
# 2. Ubah agar menjadi descending.
#=========================================================
def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key

    return data
angka1= [5,7,2,7,4,1]
print(insertion_sort(angka1))

def insertion_sort_descending(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] < key:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key

    return data

angka2= [5,7,2,7,4,1]
print(insertion_sort_descending(angka2))