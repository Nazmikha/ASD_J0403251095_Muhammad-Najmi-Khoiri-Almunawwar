#====================================================
# Nama : Muhammad Najmi Khoiri Almunawwar
# NIM : J0403251095
# Kelas : TPL B2
#====================================================
# Latihan 3  : Membuat Traversal Preorder
#======================================

# class node digunakan untuk dasar tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None # child kiri
        self.right = None # child kanan
        pass
    
# Fungsi preorder : Root > Left > Right
def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)
        
# Membuat Root
root = Node("A")
    
# Membuat child level 1
root.left = Node("B")
root.right = Node("C")
    
# Membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

root.right.right = Node("F")

# Menjalankan fungsi preorder
print("Preorder Traversal: ", end="")
preorder(root)


# Penjelasan singkat program di atas:
# Dengan tree yang sama. 
# kita membuat fungsi Traversal Preorder untuk menampilkan isi node tree dengan urutan Root > Left > Right. (cth: A > C > B)
# Kemudian menjalankan fungsi preorder untuk menampilkan isi node tree sesuai dengan urutan yang telah ditentukan.