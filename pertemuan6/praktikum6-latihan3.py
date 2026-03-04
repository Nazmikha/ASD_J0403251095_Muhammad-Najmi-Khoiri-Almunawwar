# ====================================================
# Nama = Muhammad Najmi Khoiri Almunawwar
# NIM = J0403251095
# Kelas = TPL B2
# ====================================================
# Latihan  3 . Tracing Insertion Sort
# =====================================================

def insertion_sort(data):
    # Loop pertama mulai dari data ke 2 (index array ke 1)
    for i in range(1, len(data)):
        
        # Melihat data awal
        print ("Data Awal:", data) 
        print("="*40)   

        
        key = data[i] # simpan nilai yang disisipkan 
        j = i-1 # index elemen terakhir di bagian kiri
        
        
        print("Iterasi ke-", i)
        print("Nilai Key", key)
       
        print("Bagian Kiri (Terurut): ", data[:i])
        print("Bagian Kanan(Belum Terurut): ", data[i:])
        
        # Menggeser key ke j-1
        while j >= 0 and data[j] > key:
            data[j+1] = data[j]
            j -= 1
           
            # Sisipkan key ke posisi yang benar
        data[j+1] = key
        
        print("Setelah disisipkan : ", data)
        print("-"* 50)
    return data
    
angka = [5,2,4,6,1,3]

print ("Hasil Sorting : " ,insertion_sort(angka))

#===========================================================
# Soal
# 1. Tuliskan isi list setelah iterasi i = 1.
# 2. Tuliskan isi list setelah iterasi i = 3.
# 3. Berapa kali pergeseran terjadi pada iterasi i = 4?
#==========================================================
# Jawaban
# 1
# Iterasi ke- 1
# Nilai Key 2
# Bagian Kiri (Terurut):  [5]
# Bagian Kanan(Belum Terurut):  [2, 4, 6, 1, 3]
# Setelah disisipkan :  [2, 5, 4, 6, 1, 3]

# 2 
# Iterasi ke- 3
# Nilai Key 6
# Bagian Kiri (Terurut):  [2, 4, 5]
# Bagian Kanan(Belum Terurut):  [6, 1, 3]
# Setelah disisipkan :  [2, 4, 5, 6, 1, 3]

# 3
# Ada 4 Pergeseran di Iterasi ke-4