#====================================================
# Nama : Muhammad Najmi Khoiri Almunawwar
# NIM : J0403251095
# Kelas : TPL B2
#====================================================
# Latihan 5  : Membuat Traversal Postorder
#======================================

# class node digunakan untuk dasar tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None # child kiri
        self.right = None # child kanan
        pass
    

# Fungsi postorder : Left > Right > Root
def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")
    
    
# Membuat Root: 
root = Node("A")
    
# Membuat child level 1
root.left = Node("B")
root.right = Node("C")
    
# Membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

root.right.right = Node("F")

# Menjalankan fungsi Postorder
print("Postorder Traversal: ", end="")
postorder(root)


# Penjelasan singkat program di atas:
# Dengan tree yang sama.
# kita membuat fungsi Traversal Postorder untuk menampilkan isi node tree dengan urutan Left > Right > Root. (cth: B > C > A)
# Kemudian menjalankan fungsi postorder untuk menampilkan isi node tree sesuai dengan urutan yang telah ditentukan.
