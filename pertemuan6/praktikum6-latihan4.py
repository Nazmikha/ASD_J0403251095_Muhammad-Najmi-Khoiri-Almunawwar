# ====================================================
# Nama = Muhammad Najmi Khoiri Almunawwar
# NIM = J0403251095
# Kelas = TPL B2
# ====================================================
# Latihan   4 . Memahami Kode Program (Merge Sort)
# =====================================================

def merge_sort(data):
    
    if len(data) <= 1:
        return data
        
    
    mid = len(data) //2
    left = data[:mid] 
    right = data[mid:] 
    
 
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    
    return merge(left_sorted, right_sorted)
#==========================================================
# Soal
# 1. Apa yang dimaksud dengan base case?
# 2. Mengapa fungsi memanggil dirinya sendiri?
# 3. Apa tujuan fungsi merge()?
#========================================================
# Jawaban
# 1
# Base case adalah kondisi default atau metode untuk memberhentikan fungsi rekursif
# 2
# Karena didalam fungsi tersebut terdapat baris program yang memanggil fungsi itu sendiri
# 3
# Fungsi merge() bertujuan untuk menggabungkan 2 list yang tidak terurut menjadi 1 list yang terurutt