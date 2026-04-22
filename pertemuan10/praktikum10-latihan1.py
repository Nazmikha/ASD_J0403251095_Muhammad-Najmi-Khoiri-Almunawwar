# ==========================================================
# Nama    : Muhammad Najmi Khoiri Almunawwar
# NIM     : J0403251095
# Judul   : Latihan 1-3: Node BST, Insert, Traversal Inorder, dan Search
# Modul   : Modul 6 - Binary Search Tree (BST) dan AVL Tree
# Matkul  : Algoritma dan Struktur Data (TPL2106)
# ==========================================================


# ==========================================================
# LATIHAN 1: Membuat Node dan BST (Insert)
# ==========================================================

# Kelas Node adalah representasi satu simpul (node) dalam BST.
# Setiap node menyimpan satu nilai data, pointer ke anak kiri, dan pointer ke anak kanan.
class Node:
    def __init__(self, data):
        self.data  = data   # nilai yang disimpan di node ini
        self.left  = None   # pointer ke anak kiri (nilai lebih kecil)
        self.right = None   # pointer ke anak kanan (nilai lebih besar)


# Fungsi insert menyisipkan nilai baru ke dalam BST secara rekursif.
# Aturan BST: nilai < node → masuk subtree kiri; nilai > node → masuk subtree kanan.
# Parameter  : root (node akar saat ini), data (nilai yang ingin disisipkan)
# Return     : node akar yang telah diperbarui
def insert(root, data):
    # Base case: jika posisi ini kosong, buat node baru di sini
    if root is None:
        return Node(data)

    if data < root.data:
        # Nilai lebih kecil → terus rekursi ke subtree kiri
        root.left = insert(root.left, data)
    elif data > root.data:
        # Nilai lebih besar → terus rekursi ke subtree kanan
        root.right = insert(root.right, data)
    # Jika data == root.data, nilai duplikat tidak disisipkan (diabaikan)

    return root  # kembalikan root agar struktur tree tetap terhubung


# --- Program utama Latihan 1 ---
root = None  # mulai dari tree kosong

# Daftar data yang akan disisipkan ke BST
data_list = [50, 30, 70, 20, 40, 60, 80]

# Sisipkan setiap nilai satu per satu ke dalam BST
for data in data_list:
    root = insert(root, data)

print("=" * 40)
print("LATIHAN 1: BST berhasil dibuat")
print(f"Data yang dimasukkan: {data_list}")
# Hasil tree yang terbentuk:
#        50
#       /  \
#      30   70
#     / \  / \
#    20 40 60 80


# ==========================================================
# LATIHAN 2: Traversal Inorder (Sorting Otomatis)
# ==========================================================
# Traversal Inorder mengunjungi node dalam urutan: Kiri → Root → Kanan.
# Sifat BST menjamin bahwa inorder traversal selalu menghasilkan urutan data yang TERURUT NAIK (ascending).

# Fungsi inorder mencetak semua nilai dalam BST secara terurut.
# Parameter : root (node yang sedang dikunjungi)
def inorder(root):
    if root is not None:
        inorder(root.left)              # kunjungi semua node di subtree kiri terlebih dahulu
        print(root.data, end=" ")       # cetak nilai node saat ini
        inorder(root.right)             # lalu kunjungi semua node di subtree kanan


print("\n" + "=" * 40)
print("LATIHAN 2: Traversal Inorder (urutan terurut naik):")
print("Hasil inorder: ", end="")
inorder(root)
# Output yang diharapkan: 20 30 40 50 60 70 80
print()  # baris baru setelah output inorder


# ==========================================================
# LATIHAN 3: Searching (Pencarian Nilai)
# ==========================================================
# Pencarian pada BST memanfaatkan sifat urutan BST agar lebih efisien.
# Setiap langkah membuang setengah dari sisa tree (mirip binary search).

# Fungsi search mencari nilai key di dalam BST secara rekursif.
# Parameter : root (node yang sedang diperiksa), key (nilai yang dicari)
# Return    : True jika ditemukan, False jika tidak
def search(root, key):
    # Base case: tree habis (atau posisi kosong) → nilai tidak ada
    if root is None:
        return False

    if root.data == key:
        # Nilai ditemukan tepat di node ini
        return True
    elif key < root.data:
        # Nilai yang dicari lebih kecil → cari di subtree kiri
        return search(root.left, key)
    else:
        # Nilai yang dicari lebih besar → cari di subtree kanan
        return search(root.right, key)


print("\n" + "=" * 40)
print("LATIHAN 3: Search BST")

# Uji pencarian untuk beberapa nilai
for key in [40, 10, 80, 55]:
    hasil = search(root, key)
    if hasil:
        print(f"  Pencarian {key}: DITEMUKAN ✓")
    else:
        print(f"  Pencarian {key}: Tidak ditemukan ✗")

# -----------------------------------------------------------
# DISKUSI & PENJELASAN
# -----------------------------------------------------------
# 1. BST menyimpan data dengan aturan: kiri < root < kanan, sehingga
#    pencarian bisa membuang setengah tree di setiap langkah → O(log n)
#    pada kasus tree seimbang.
# 2. Inorder traversal pada BST secara otomatis menghasilkan urutan ascending
#    tanpa perlu algoritma sorting tambahan.
# 3. Nilai duplikat diabaikan pada fungsi insert di atas agar BST tetap valid.
# -----------------------------------------------------------
