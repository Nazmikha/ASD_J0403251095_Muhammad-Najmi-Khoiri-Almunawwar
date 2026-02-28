# =====================================================
# Nama : Muhammad Najmi Khoiri Almunawwar
# NIM : J0403251095 
# ====================================================
# Implementasi Dasar : Node pada Linked List
# ====================================================

# Membuat class node (merupakan struktur dasar dari linked list)
class node : 
    def __init__(self, data) : # Constructor untuk inisialisasi node
        self.data = data # Menyimpan Nilai/data
        self.next = None # Pointer untuk node selanjutnya

# Proses 1) Membuat node satu per satu
nodeA = node("A") 
nodeB = node("B") 
nodeC = node("C") 

# Proses 2) Menghubungkan node : A -> B -> C -> none
nodeA.next = nodeB # Node A menunjuk ke Node B
nodeB.next = nodeC # Node B menunjuk ke Node C

# Proses 3) Menentukan node pertama 
head = nodeA # Node A sebagai head

# Proses 4) Traversal : Menampilkan data dari node pertama hingga akhir
current = head # Mulai dari head
while current is not None : # Selama masih ada node yang dapat diakses
    print(current.data) # Tampilkan data dari node saat ini
    current = current.next # Pindah ke node berikutnya
    
# ====================================================================================
# Implementasi Dasar : Linked List + Insert Awal
# ====================================================================================

class LinkedList :
    def __init__(self) : # Constructor untuk inisialisasi linked list
        self.head = None # Pointer untuk node pertama (head)
    
    
    def insert_awal(self, data): # Konsep Push pada Stack (LIFO) : Insert di awal linked list
        #Buat node baru dengan data yang diberikan
        nodeBaru = node(data) # Membuat node baru dengan data yang diberikaa
        nodeBaru.next = self.head # Node baru menunjuk ke node yang saat ini menjadi head
        self.head = nodeBaru # Node baru menjadi head yang baru
        
    def tampilkan(self): #Implementasi traversal
        current = self.head # Mulai dari head
        while current is not None : # Selama masih ada node yang dapat diakses
            print(current.data) # Tampilkan data dari node saat ini 
            current = current.next # Pindah ke node berikutnya
            
    def hapus_awal(self):# Konsep Pop pada Stack (LIFO) : Hapus di awal linked list
        data_terhapus = self.head.data # Peek dalam stack
        # Menggeser head ke node berikutnya
        self.head= self.head.next        
        print( "Node yang dihapus adalah:", data_terhapus) # Tampilkan data yang dihapus

print ("============== List Baru =================")            
ll = LinkedList() # Membuat instatiasi objek ke class linked list
ll.insert_awal("X") # Menambahkan node dengan data "C" di awal linked list 
ll.insert_awal("Y") # Menambahkan node dengan data "B" di awal linked list
ll.insert_awal("Z") # Menambahkan node dengan data "A" di awal linked list
ll.tampilkan() # Menampilkan isi linked list setelah penambahan node baru di awal
# Menghapus node pertama (head) dari linked list
ll.hapus_awal() # Menghapus node pertama (head) dari linked list
ll.tampilkan() # Menampilkan isi linked list setelah penghapusan node pertama (head)