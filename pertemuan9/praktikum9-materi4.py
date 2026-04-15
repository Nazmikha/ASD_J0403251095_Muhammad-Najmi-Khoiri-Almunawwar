#====================================================
# Nama : Muhammad Najmi Khoiri Almunawwar
# NIM : J0403251095
# Kelas : TPL B2
#====================================================
# Latihan 4  : Membuat Traversal Inorder
#======================================

# class node digunakan untuk dasar tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None # child kiri
        self.right = None # child kanan
        pass

# Fungsi inorder : Left > Root > Right
def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)
        
        
# Membuat Root
root = Node("A")
    
# Membuat child level 1
root.left = Node("B")
root.right = Node("C")
    
# Membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

root.right.right = Node("F")

# Menjalankan fungsi inorder
print("Inorder Traversal: ", end="")
inorder(root)

# Penjelasan singkat program di atas:
# Dengan tree yang sama.
# kita membuat fungsi Traversal Inorder untuk menampilkan isi node tree dengan urutan Left > Root > Right. (cth: B > A > C)
# Kemudian menjalankan fungsi inorder untuk menampilkan isi node tree sesuai dengan urutan yang telah ditentukan.
