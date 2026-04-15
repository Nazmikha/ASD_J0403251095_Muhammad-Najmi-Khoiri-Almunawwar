#====================================================
# Nama : Muhammad Najmi Khoiri Almunawwar
# NIM : J0403251095
# Kelas : TPL B2
#====================================================
# Latihan 5  : Struktur Organisasi Perusahaan
#======================================

# class node digunakan untuk dasar tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None # child kiri
        self.right = None # child kanan
        pass

# Membuat tree struktur organisasi perusahaan
root = Node("Direktur")

# Child Level 1
root.left = Node("Manajer A")
root.right = Node("Manajer B")

# Child Level 2
root.left.left = Node("Staff 1")
root.left.right = Node("Staff 2")

root.right.right = Node("Staff 3")

# Fungsi preorder : Root > Left > Right
def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)


# Menjalankan fungsi preorder
print("Struktur Organisasi (Preorder): ")
preorder(root)

# Penjelasan singkat program di atas:
# Kita membuat tree yang merepresentasikan struktur organisasi perusahaan dengan root sebagai Direktur,
# kemudian child level 1 sebagai Manajer A dan Manajer B, serta child level 2 sebagai Staff 1, Staff 2, dan Staff 3.
# Kemudian kita menggunakan fungsi preorder untuk menampilkan struktur organisasi dengan urutan Root > Left > Right. (cth: Direktur > Manajer A > Staff 1 > Staff 2 > Manajer B > Staff 3)
