# ==========================================================
# Nama    : Muhammad Najmi Khoiri Almunawwar
# NIM     : J0403251095
# Judul   : Latihan 5: Rotasi Kiri pada BST Tidak Seimbang
# Modul   : Modul 6 - Binary Search Tree (BST) dan AVL Tree
# Matkul  : Algoritma dan Struktur Data (TPL2106)
# ==========================================================
#
# KONSEP ROTASI KIRI (Left Rotation / kasus RR):
# Digunakan ketika tree miring ke KANAN (balance factor < -1).
# Node anak kanan naik menggantikan posisi root lama.
#
# Sebelum rotasi kiri:      Sesudah rotasi kiri:
#   10                           20
#     \                         /  \
#     20          →            10  30
#       \
#       30
#
# Langkah rotasi kiri pada node x (root lama = 10):
#   1. y   = x.right       → y  = 20 (calon root baru)
#   2. T2  = y.left        → T2 = None (subtree kiri y yang akan dipindah)
#   3. y.left  = x         → 10 menjadi anak kiri dari 20
#   4. x.right = T2        → anak kanan 10 diganti T2 (None)
#   5. return y            → 20 menjadi root baru
# ==========================================================


# Kelas Node menyimpan satu elemen data beserta pointer ke anak kiri dan kanan.
class Node:
    def __init__(self, data):
        self.data  = data   # nilai node
        self.left  = None   # anak kiri
        self.right = None   # anak kanan


# Fungsi preorder mencetak nilai dengan urutan Root → Kiri → Kanan.
# Digunakan untuk memverifikasi isi tree sebelum dan sesudah rotasi.
def preorder(root):
    if root is not None:
        print(root.data, end=" ")  # cetak nilai node saat ini
        preorder(root.left)        # kunjungi subtree kiri
        preorder(root.right)       # kunjungi subtree kanan


# Fungsi tampil_struktur menampilkan hierarki tree secara visual (indentasi).
# level   : kedalaman node (bertambah 1 setiap turun satu tingkat)
# posisi  : label "Root", "L" (kiri), atau "R" (kanan)
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        print("  " * level + f"{posisi}: {root.data}")  # cetak dengan indentasi
        tampil_struktur(root.left,  level + 1, "L")     # rekursi ke kiri
        tampil_struktur(root.right, level + 1, "R")     # rekursi ke kanan


# Fungsi rotate_left melakukan rotasi kiri pada node x.
# Rotasi kiri digunakan untuk menyeimbangkan tree yang condong ke kanan (kasus RR).
# Parameter : x (node yang menjadi pivot rotasi / root lama)
# Return    : y (node yang menjadi root baru setelah rotasi)
def rotate_left(x):
    y  = x.right    # y adalah anak kanan x → akan menjadi root baru
    T2 = y.left     # simpan subtree kiri milik y (akan dipindahkan ke kanan x)

    # --- Proses rotasi ---
    y.left  = x     # x turun menjadi anak kiri dari y
    x.right = T2    # anak kanan x diisi oleh T2 (subtree yang tadi dimiliki y)

    # y kini menjadi root baru; kembalikan y ke pemanggil
    return y


# --- Program Utama ---

# Buat tree yang TIDAK SEIMBANG secara manual (condong ke kanan):
#   10
#     \
#     20
#       \
#       30
root              = Node(10)   # root / simpul paling atas
root.right        = Node(20)   # 20 adalah anak kanan dari 10
root.right.right  = Node(30)   # 30 adalah anak kanan dari 20

print("=" * 45)
print("LATIHAN 5: Rotasi Kiri pada BST Tidak Seimbang")
print()

# Tampilkan kondisi tree SEBELUM rotasi
print("Preorder SEBELUM rotasi kiri:")
preorder(root)
print()

print("\nStruktur SEBELUM rotasi kiri:")
tampil_struktur(root)

# Lakukan rotasi kiri pada root sehingga 20 naik menjadi root baru
root = rotate_left(root)

# Tampilkan kondisi tree SESUDAH rotasi
print("\nPreorder SESUDAH rotasi kiri:")
preorder(root)
print()

print("\nStruktur SESUDAH rotasi kiri:")
tampil_struktur(root)

# -----------------------------------------------------------
# DISKUSI
# -----------------------------------------------------------
# Setelah rotasi kiri:
#      20
#     /  \
#    10  30
#
# Tree kini seimbang: root = 20, anak kiri = 10, anak kanan = 30.
# Balance factor setiap node bernilai 0 → tree valid sebagai AVL Tree.
#
# Rotasi kiri hanya mengubah POINTER antar node; nilai data tidak berubah
# sama sekali, sehingga properti BST (kiri < root < kanan) tetap terjaga.
#
# Output yang diharapkan:
# Preorder SEBELUM: 10 20 30
# Preorder SESUDAH: 20 10 30
#
# Struktur SESUDAH:
# Root: 20
#   L: 10
#   R: 30
# -----------------------------------------------------------
