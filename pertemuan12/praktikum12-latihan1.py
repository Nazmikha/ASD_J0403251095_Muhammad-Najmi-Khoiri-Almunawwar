# ==========================================================
# Nama    : Muhammad Najmi Khoiri Almunawwar
# NIM     : J0403251095
# Kelas   : TPL B
# Praktikum 12 - Latihan 1: Weighted Graph dan Perhitungan Jalur
# ==========================================================

graph = {
    'A': {'B': 4, 'C': 2},   # Dari A bisa ke B (bobot 4) atau C (bobot 2)
    'B': {'D': 5},             # Dari B hanya bisa ke D (bobot 5)
    'C': {'D': 1},             # Dari C hanya bisa ke D (bobot 1)
    'D': {}                    # D adalah node tujuan, tidak ada edge keluar
}


# Menghitung dua kemungkinan jalur dari A ke D 
jalur_1 = graph['A']['B'] + graph['B']['D']   # 4 + 5 = 9

jalur_2 = graph['A']['C'] + graph['C']['D']   # 2 + 1 = 3

print("=" * 40)
print("  Latihan 1: Weighted Graph & Jalur")
print("=" * 40)
print(f"Jalur 1 (A → B → D) = {graph['A']['B']} + {graph['B']['D']} = {jalur_1}")
print(f"Jalur 2 (A → C → D) = {graph['A']['C']} + {graph['C']['D']} = {jalur_2}")
print()

# Bandingkan kedua jalur dan tentukan mana yang terpendek
if jalur_1 < jalur_2:
    print(f"Jalur terpendek: A → B → D (total bobot = {jalur_1})")
else:
    print(f"Jalur terpendek: A → C → D (total bobot = {jalur_2})")


# ==========================================================
# JAWABAN ANALISIS
# ==========================================================

# 1. Berapa total bobot jalur A → B → D?
#    → Total bobot = 4 (A→B) + 5 (B→D) = 9

# 2. Berapa total bobot jalur A → C → D?
#    → Total bobot = 2 (A→C) + 1 (C→D) = 3

# 3. Jalur mana yang dipilih sebagai jalur terpendek?
#    → Jalur A → C → D dengan total bobot 3.
#      Meskipun kedua jalur sama-sama melewati 2 edge,
#      jalur kedua memiliki total bobot yang jauh lebih kecil.

# 4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge paling sedikit?
#    → Karena pada weighted graph, setiap edge memiliki bobot (biaya) yang berbeda.
#      Algoritma shortest path berfokus pada TOTAL BIAYA MINIMUM, bukan jumlah langkah.
#      Contoh: jalur dengan 3 edge berbobot total 4 lebih baik dari jalur
#      2 edge berbobot total 9. Jalur terpendek = jalur termurah, bukan terpendek
#      dalam jumlah node/edge yang dilalui.
# ==========================================================
