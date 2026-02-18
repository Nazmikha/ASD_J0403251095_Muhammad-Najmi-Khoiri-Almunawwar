# ==================================================
# Nama : Muhammad Najmi Khoiri Almunawwar
# NIM : J0403251095
# ==================================================
# Implementasi Dasar : Queue berbasis Linked List
# ==================================================

class node : 
    def __init__(self, data) : # Constructor untuk inisialisasi node
        self.data = data # Menyimpan Nilai/data
        self.next = None # Pointer untuk node selanjutnya
        
# Queue dengan 2 Pointer : front dan rear
class QueueLL :
    def __init__(self):
        self.front = None # Pointer untuk node pertama (front)
        self.rear = None # Pointer untuk node terakhir (rear)
    
    def enqueue(self,data):
        # Menambah data di belakang (rear)
        nodeBaru = node(data)        
        
        #Jika queue kosong, front dan rear menunjuk ke node yang sama
        if self.rear is None and self.front is None :
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        
        # Jika queue tidak kosong :
        # Rear lama menunjuk ke node baru 
        self.rear.next = nodeBaru
        # Rear pindah ke node baru
        self.rear = nodeBaru
        
    def dequeue(self,data):
        #Menghapus data dari depan
        # 1) Lihat data paling depan
        data_terhapus = self.front.data
        # 2) Geser front ke node berikutnya
        self.front = self.front.next
        # 3) Jika setelah geser front menjadi none, maka queue kosong
        # rear juga harus jadi none
        if self.front is None :
            self.rear = None
            
        return data_terhapus
        
    def tampilkan(self):
        # Menampilkan isi queue 
        current = self.front 
        print("Front", end="->")
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print ("Rear")
        
        
        
# Instantiasi objek class QueueLL
q = QueueLL()

q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()
# hapus data
q.dequeue("A")
q.tampilkan()
