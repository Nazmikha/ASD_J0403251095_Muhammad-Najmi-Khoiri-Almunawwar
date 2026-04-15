#====================================================
# Nama : Muhammad Najmi Khoiri Almunawwar
# NIM : J0403251095
# Kelas : TPL B2
#====================================================
# Latihan 2 : Menampilkan Isi Node Tree
#======================================

# class node digunakan untuk dasar tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None # child kiri
        self.right = None # child kanan
        pass
# Membuat Root
root = Node("A")
    
# Membuat child level 1
root.left = Node("B")
root.right = Node("C")
    
# Membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

root.right.left = Node("F")
root.right.right = Node("G")
    
# Menampilkan isi Node 
print("Data pada root: ", root.data)
print("Child kiri root: ", root.left.data)
print("Child kanan root: ", root.right.data)
print("Child kiri child dari Node B: ", root.left.left.data)
print("Child kanan child dari Node B: ", root.left.right.data)
print("Child kiri child dari Node C: ", root.right.left.data)
print("Child kanan child dari Node C: ", root.right.right.data)


# Penjelasan singkat program di atas:
# Lanjutan dari latihan 1, menambahkan lagi node child untuk melengkapi tree yang ada hingga huruf G.
# dengan format root.left.left/right untuk mengakses child kiri/kanan dari child kiri root, begitu juga dengan sisi root.right. Kemudian menampilkan isi node tree sesuai dengan urutan yang telah ditentukan. 