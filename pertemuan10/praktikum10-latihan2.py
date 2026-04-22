# ==========================================================
# Nama    : Muhammad Najmi Khoiri Almunawwar
# NIM     : J0403251095
# Judul   : Latihan 4: Membuat BST yang Tidak Seimbang
# ==========================================================
#
# KONSEP:
# Jika data dimasukkan dalam urutan yang sudah terurut (ascending maupun
# descending), BST akan "miring" ke satu sisi dan menyerupai Linked List.
# Contoh: memasukkan 10, 20, 30 secara berurutan menghasilkan:
#
#   10
#    \
#    20
#      \
#      30
#
# Tree seperti ini dikatakan TIDAK SEIMBANG karena semua node condong ke kanan.
# Akibatnya, operasi search menjadi O(n) alih-alih O(log n).
# ==========================================================


# Kelas Node menyimpan satu elemen data beserta pointer ke anak kiri dan kanan.
class Node:
    def __init__(self, data):
        self.data  = data   # nilai yang disimpan di node
        self.left  = None   # anak kiri (nilai lebih kecil)
        self.right = None   # anak kanan (nilai lebih besar)


# Fungsi insert menyisipkan nilai ke BST secara rekursif.
# Karena tidak ada mekanisme penyeimbangan, tree bisa menjadi miring
# jika data dimasukkan secara berurutan.
def insert(root, data):
    if root is None:
        # Posisi kosong ditemukan → tempatkan node baru di sini
        return Node(data)

    if data < root.data:
        # Nilai lebih kecil dari node saat ini → lanjut ke kiri
        root.left = insert(root.left, data)
    elif data > root.data:
        # Nilai lebih besar dari node saat ini → lanjut ke kanan
        root.right = insert(root.right, data)

    return root  # kembalikan root agar tree tetap terhubung


# Fungsi preorder mencetak nilai tree dengan urutan: Root → Kiri → Kanan.
# Berguna untuk melihat nilai root terlebih dahulu sebelum anak-anaknya.
def preorder(root):
    if root is not None:
        print(root.data, end=" ")  # cetak node saat ini
        preorder(root.left)        # kunjungi subtree kiri
        preorder(root.right)       # kunjungi subtree kanan


# Fungsi tampil_struktur menampilkan hierarki tree secara visual di terminal.
# Parameter level  : kedalaman node saat ini (digunakan untuk indentasi)
# Parameter posisi : label posisi node ("Root", "L" untuk kiri, "R" untuk kanan)
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        # Cetak indentasi sebanyak 'level' spasi lalu tampilkan posisi dan nilai
        print("  " * level + f"{posisi}: {root.data}")
        # Rekursi ke anak kiri dengan kedalaman bertambah 1
        tampil_struktur(root.left,  level + 1, "L")
        # Rekursi ke anak kanan dengan kedalaman bertambah 1
        tampil_struktur(root.right, level + 1, "R")


# --- Program Utama ---
root = None

# Data dimasukkan BERURUTAN NAIK → menyebabkan tree condong ke kanan
# Setiap nilai baru selalu lebih besar dari sebelumnya sehingga selalu
# masuk ke subtree kanan, membentuk rantai panjang ke kanan.
data_list = [10, 20, 30]

for data in data_list:
    root = insert(root, data)

print("=" * 40)
print("LATIHAN 4: BST Tidak Seimbang")
print(f"Data yang dimasukkan (berurutan): {data_list}")
print()

# Tampilkan hasil traversal preorder
print("Preorder BST:")
preorder(root)
print()

# Tampilkan visualisasi struktur tree
print("\nStruktur BST:")
tampil_struktur(root)

# -----------------------------------------------------------
# CHECKPOINT & DISKUSI
# -----------------------------------------------------------
# 1. Tree condong ke KANAN karena data 10 → 20 → 30 selalu makin besar,
#    sehingga setiap node baru masuk ke kanan node sebelumnya.
#
# 2. Semakin panjang "rantai" ini, pencarian makin LAMBAT karena setiap
#    operasi search harus memeriksa node satu per satu dari atas ke bawah,
#    persis seperti Linked List → kompleksitas O(n), bukan O(log n).
#
# 3. BST TIDAK SELALU SEIMBANG. Urutan penyisipan data sangat menentukan
#    bentuk tree. Untuk menjamin keseimbangan digunakan AVL Tree atau
#    struktur self-balancing lainnya.
#
# Output yang diharapkan:
# Preorder BST:
# 10 20 30
#
# Struktur BST:
# Root: 10
#   R: 20
#     R: 30
# -----------------------------------------------------------
