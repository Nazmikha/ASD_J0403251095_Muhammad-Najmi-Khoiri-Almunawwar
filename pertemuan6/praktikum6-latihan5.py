# ====================================================
# Nama = Muhammad Najmi Khoiri Almunawwar
# NIM = J0403251095
# Kelas = TPL B2
# ====================================================
# Latihan   5 . Melengkapi Fungsi Merge
# =====================================================
# def merge(left, right):
#  result = []
#  i = 0
#  j = 0
# 
#  while i < len(left) and j < len(right):
#  if __________________________:
#  reult.append(left[i])
#  i += 1
#  else:
#  result.append(right[j])
#  j += 1
# 
#  result.extend(left[i:])
#  result.extend(right[j:])

#  return result
#=================================================
# Soal
# 1. Lengkapi kondisi agar menjadi ascending.
# 2. Jelaskan fungsi result.extend().
#==================================================
# Jawaban
# 1
def merge(left, right):
    
    result = []
    i = 0
    j = 0
    
    # Membandingkan elemen kiri dengan kanan
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j=+1
            
        # Menambahkan sisa elemen jika ada
        result.extend(left[i:])
        result.extend(right[j:])
        
        return result
# 2
# Funsgi Result.extend adalah untuk menambahkan kelompok elemen yang telah di sorting ke dalam resultt