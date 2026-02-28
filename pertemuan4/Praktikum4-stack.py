#========IDENTITAS MAHASISWA===================
#NAMA : Muhammad Najmi Khoiri Almunawwar
#NIM  : J0403251095
#Kelas: P2
#================================================

# ==========================================================
# Implementasi Dasar: Stack (LIFO) berbasis Linked List
# ==========================================================

# ----------------------------------------------------------
# Definisi class Node (unit dasar dari Linked List)
# ----------------------------------------------------------
class Node:
    def __init__(self, data):
        self.data = data  # menyimpan nilai/data
        self.next = None  # pointer ke node berikutnya (awal: None)


# ----------------------------------------------------------
# Definisi class Stack berbasis Linked List
# Menggunakan prinsip LIFO (Last In First Out)
# ----------------------------------------------------------
class Stack:
    def __init__(self):
        self.top = None  # top menunjuk node paling atas (awalnya kosong)

    def is_empty(self):
        # Stack kosong jika top = None
        return self.top is None

    def push(self, data):
        # push artinya menambahkan elemen baru ke paling atas stack
        # 1) Buat node baru
        node_baru = Node(data)
        # 2) Node baru menunjuk ke top lama
        node_baru.next = self.top
        # 3) Top berpindah ke node baru
        self.top = node_baru

    def pop(self):
        # pop artinya mengambil dan menghapus elemen paling atas stack
        if self.is_empty():
            print("Stack kosong, tidak bisa pop.")
            return None
        # Simpan data yang akan diambil
        data_terambil = self.top.data
        # Geser top ke node berikutnya (node di bawahnya)
        self.top = self.top.next
        return data_terambil

    def peek(self):
        # peek melihat data paling atas tanpa menghapus node
        if self.is_empty():
            return None
        return self.top.data

    def tampilkan(self):
        # Menampilkan isi stack dari top ke bawah
        current = self.top
        print("Top -> ", end="")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next  # pindah ke node berikutnya
        print("None")


# ----------------------------------------------------------
# Program Utama: Menguji operasi Stack
# ----------------------------------------------------------
s = Stack()

# Melakukan push data A, B, C ke dalam stack
s.push("A")
s.push("B")
s.push("C")

# Menampilkan isi stack setelah push A, B, C
print("Isi stack setelah push A, B, C:")
s.tampilkan()

# Melihat data paling atas tanpa menghapus (peek)
print("Peek (lihat top):", s.peek())

# Mengambil data dari paling atas stack (pop)
data = s.pop()
print("Pop mengembalikan:", data)

# Menampilkan isi stack setelah pop
print("Isi stack setelah pop:")
s.tampilkan()
