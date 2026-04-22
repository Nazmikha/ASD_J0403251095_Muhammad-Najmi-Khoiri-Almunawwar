# ==========================================================
# Nama    : Muhammad Najmi Khoiri Almunawwar
# NIM     : J0403251095
# Judul   : Latihan 6: Rotasi Kanan pada BST Tidak Seimbang (TUGAS)
# Modul   : Modul 6 - Binary Search Tree (BST) dan AVL Tree
# Matkul  : Algoritma dan Struktur Data (TPL2106)
# ==========================================================
#
# KONSEP ROTASI KANAN (Right Rotation / kasus LL):
# Digunakan ketika tree miring ke KIRI (balance factor > 1).
# Node anak KIRI naik menggantikan posisi root lama.
#
# Sebelum rotasi kanan:     Sesudah rotasi kanan:
#     30                          20
#    /                           /  \
#   20            →             10  30
#  /
# 10
#
# Langkah rotasi kanan pada node y (root lama = 30):
#   1. x   = y.left        → x  = 20 (calon root baru)
#   2. T2  = x.right       → T2 = None (subtree kanan x yang akan dipindah)
#   3. x.right = y         → 30 menjadi anak kanan dari 20
#   4. y.left  = T2        → anak kiri 30 diganti T2 (None)
#   5. return x            → 20 menjadi root baru
# ==========================================================


# Kelas Node menyimpan satu elemen data beserta pointer ke anak kiri dan kanan.
class Node:
    def __init__(self, data):
        self.data  = data   # nilai yang disimpan di node
        self.left  = None   # pointer ke anak kiri (nilai lebih kecil)
        self.right = None   # pointer ke anak kanan (nilai lebih besar)


# Fungsi preorder mencetak nilai dengan urutan Root → Kiri → Kanan.
# Berguna untuk memverifikasi isi dan urutan node dalam tree.
def preorder(root):
    if root is not None:
        print(root.data, end=" ")  # cetak nilai node saat ini
        preorder(root.left)        # kunjungi subtree kiri
        preorder(root.right)       # kunjungi subtree kanan


# Fungsi tampil_struktur menampilkan hierarki tree secara visual menggunakan indentasi.
# level   : kedalaman node saat ini (bertambah 1 tiap turun satu level)
# posisi  : label "Root", "L" (anak kiri), atau "R" (anak kanan)
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        print("  " * level + f"{posisi}: {root.data}")  # cetak dengan indentasi
        tampil_struktur(root.left,  level + 1, "L")     # rekursi ke anak kiri
        tampil_struktur(root.right, level + 1, "R")     # rekursi ke anak kanan


# Fungsi rotate_right melakukan rotasi kanan pada node y.
# Rotasi kanan digunakan untuk menyeimbangkan tree yang condong ke KIRI (kasus LL).
# Parameter : y (node pivot / root lama yang akan "turun" ke kanan)
# Return    : x (node yang naik menjadi root baru setelah rotasi)
def rotate_right(y):
    x  = y.left     # x adalah anak kiri y → akan naik menjadi root baru
    T2 = x.right    # simpan subtree kanan milik x (akan dipindahkan ke kiri y)

    # --- Proses rotasi ---
    x.right = y     # y turun menjadi anak kanan dari x
    y.left  = T2    # anak kiri y diisi oleh T2 (subtree yang tadi dimiliki x)

    # x kini menjadi root baru; kembalikan x ke pemanggil
    return x


# --- Program Utama ---

# Buat tree yang TIDAK SEIMBANG secara manual (condong ke kiri):
# Data: 30, 20, 10 dimasukkan berurutan menurun.
# Karena setiap nilai baru lebih kecil dari sebelumnya,
# setiap node baru selalu masuk ke subtree KIRI.
#
#   30
#  /
# 20
# /
# 10

root             = Node(30)   # root / simpul paling atas
root.left        = Node(20)   # 20 adalah anak kiri dari 30
root.left.left   = Node(10)   # 10 adalah anak kiri dari 20

print("=" * 45)
print("LATIHAN 6: Rotasi Kanan pada BST Tidak Seimbang")
print()

# Tampilkan kondisi tree SEBELUM rotasi
print("Preorder SEBELUM rotasi kanan:")
preorder(root)
print()

print("\nStruktur SEBELUM rotasi kanan:")
tampil_struktur(root)

# Lakukan rotasi kanan pada root:
# → 20 naik menjadi root baru
# → 10 tetap di kiri 20
# → 30 turun menjadi anak kanan 20
root = rotate_right(root)

# Tampilkan kondisi tree SESUDAH rotasi
print("\nPreorder SESUDAH rotasi kanan:")
preorder(root)
print()

print("\nStruktur SESUDAH rotasi kanan:")
tampil_struktur(root)

# -----------------------------------------------------------
# DISKUSI
# -----------------------------------------------------------
# Setelah rotasi kanan:
#      20
#     /  \
#    10  30
#
# Tree kini SEIMBANG: root = 20, anak kiri = 10, anak kanan = 30.
# Balance factor tiap node = 0 → tree valid sebagai AVL Tree.
#
# Rotasi kanan adalah KEBALIKAN dari rotasi kiri:
#   - Rotasi kiri  : dipakai saat tree condong ke kanan (kasus RR)
#   - Rotasi kanan : dipakai saat tree condong ke kiri  (kasus LL)
#
# Sama seperti rotasi kiri, rotasi kanan TIDAK mengubah nilai data,
# hanya mengubah pointer antar node, sehingga properti BST tetap terjaga.
#
# Output yang diharapkan:
# Preorder SEBELUM: 30 20 10
# Preorder SESUDAH: 20 10 30
#
# Struktur SESUDAH:
# Root: 20
#   L: 10
#   R: 30
# -----------------------------------------------------------
