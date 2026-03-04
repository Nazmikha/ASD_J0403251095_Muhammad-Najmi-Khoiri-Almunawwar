# ====================================================
# Nama = Muhammad Najmi Khoiri Almunawwar
# NIM = J0403251095
# Kelas = TPL B2
# ====================================================

# ====================================================
# Insertion Sort dengan Tracing
# ====================================================

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
    
angka = [7,8,5,2,4,6]

print ("Hasil Sorting : " ,insertion_sort(angka))


        