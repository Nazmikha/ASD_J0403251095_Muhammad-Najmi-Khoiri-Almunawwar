#====================================================
# Nama : Muhammad Najmi Khoiri Almunawwar
# NIM : J0403251095
# Kelas : TPL B2
#====================================================
# Latihan 1  : Membuat Node Tree
#====================================================

# class node digunakan untuk dasar tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None # child kiri
        self.right = None # child kanan
        pass
    
# Membuat Root
root = Node("A")
    
# Menampilkan isi Node 
print("Data pada root: ", root.data)
print("Child kiri root: ", root.left)
print("Child kanan root: ", root.right)


# Penjelasan singkat program di atas:
# Membuat class Node yang memiliki atribut data, left, dan right. Kemudian membuat sebuah node root dengan nilai "A" dan menampilkan isi dari node root beserta child kiri dan kanan yang masih None.