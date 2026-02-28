#=======================================
# Nama : Muhammad Najmi Khoiri Almunawwar
# NIM : J0403251095
# Kelas : TPL B
#========================================

#========================================
# Studi Kasus : Sistem Antrian Layanan Akademik
# Implementasi Queue ->
# Enqueue : memindahkan pointer rear ke belakang dan menambahkan elemen baru di posisi rear
# Dequeue : memindahkan pointer front ke depan dan menghapus elemen di posisi front
# Front -> A -> B -> C -> Rear
#==========================================

#1) Mendefinisikan Node (Unit dasar linked list)
class Node:
    def __init__(self, nim, nama):
        self.nim = nim # Menyimpan NIM mahasiswa
        self.nama = nama # Menyimpan nama mahasiswa
        self.next = None # Pointer ke node berikutnya

    
#2) Mendefinisikan Queue Akademik
class queueAkademik:
    def __init__(self):
        self.front = None # Pointer ke elemen depan antrian
        self.rear = None # Pointer ke elemen belakang antrian
    
    def is_empty(self):
        return self.front is None # Mengecek apakah antrian kosong
    
    def enqueue(self, nim, nama):
        nodeBaru = Node(nim, nama) # Membuat node baru dengan data mahasiswa
        
        if self.is_empty(): # Jika antrian kosong
            self.front = nodeBaru # Menjadikan node baru sebagai front
            self.rear = nodeBaru # Menjadikan node baru sebagai rear
            return
        
        #Jika queue tidak kosong, maka data baru diletakkan setelah rear kemudian dijadikan sebagai rear
        self.rear.next = nodeBaru # Menambahkan node baru di belakang antrian
        self.rear = nodeBaru # Memindahkan pointer rear ke node baru
        
    def dequeue(self):
        
        # Jika antrian kosong, tidak ada yang bisa dihapus
        if self.is_empty():
            print("Antrian kosong, tidak ada yang bisa dihapus.")
            return None
        
        # lihat data yang akan dihapus (front)
        node_hapus = self.front # Menyimpan node yang akan dihapus (front)
        
        #geser pointer front ke depan
        self.front = self.front.next # Memindahkan pointer front ke node berikutnya
        
        # jika setelah penghapusan antrian menjadi kosong, maka rear juga harus diatur ke None
        if self.front is None:
            self.rear = None # Jika antrian kosong setelah penghapusan, atur rear ke None
        
        return node_hapus # Mengembalikan node yang dihapus (front)
    
    
    def tampilkan(self): 
        
        
        print("Daftar Antrian Layanan Akademik:") # Menampilkan header daftar antrian
        current = self.front # Mulai dari front
        no = 1 # Nomor urut untuk menampilkan data
        while current is not None: # Selama masih ada node dalam antrian
            print(f"{no}. NIM: {current.nim}, Nama: {current.nama}") # Tampilkan data mahasiswa
            current = current.next # Pindah ke node berikutnya
            no += 1 # Increment nomor urut
        
    # Program utama untuk menguji implementasi queue
    
def main():
    
    #Initialisasi queue akademik
    Q = queueAkademik()
    
    while True:
        print(" ============= Sistem Antrian Layanan Akademik =============")
        print("1. Tambah Mahasiswa")
        print("2. Layani Mahasiswa")
        print("3. Tampilkan Antrian")
        print("4. Keluar")
        pilihan = input("Masukkan pilihan Anda: ").strip()
        
        if pilihan == '1':
            nim = input("Masukkan NIM : ").strip()
            nama = input("Masukkan Nama : ").strip()
            Q.enqueue(nim, nama) # Mena1mbahkan mahasiswa ke antrian
            print("Mahasiswa berhasil ditambahkan ke antrian.")
            
        elif pilihan == '2':
            dilayani = Q.dequeue()
            if dilayani is not None:
                print(f"Mahasiswa Dilayani : {dilayani.nim} - {dilayani.nama}") # Menampilkan mahasiswa yang dilayani
            else:
                print("Tidak ada mahasiswa yang dilayani karena antrian kosong.")
            
        elif pilihan == '3':
            Q.tampilkan() # Menampilkan daftar antrian
        
        elif pilihan == '4':
            print("Terima kasih telah menggunakan sistem antrian layanan akademik.")
            break
            
# Penanda eksekusi program utama            
if __name__ == "__main__":
    main()