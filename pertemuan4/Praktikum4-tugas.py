#========IDENTITAS MAHASISWA===================
#NAMA : Muhammad Najmi Khoiri Almunawwar
#NIM  : J0403251095
#Kelas: P2
#================================================

# ==========================================================
# Tugas Hands-On: Sistem Antrian Bengkel Motor
# Struktur Data: Queue (FIFO) berbasis Linked List
# ==========================================================
# Ketentuan:
# - Menggunakan class Node dan QueueBengkel
# - Memanfaatkan konsep node, pointer, dan traversal
# - Tidak menggunakan list Python sebagai struktur utama
# ==========================================================


# ----------------------------------------------------------
# 1) Definisi class Node (unit dasar Linked List)
#    Menyimpan data pelanggan: no antrian, nama, dan servis
# ----------------------------------------------------------
class Node:
    def __init__(self, no, nama, servis):
        self.no    = no      # menyimpan nomor antrian pelanggan
        self.nama  = nama    # menyimpan nama pelanggan
        self.servis = servis # menyimpan jenis servis yang diminta
        self.next  = None    # pointer ke node berikutnya (awal: None)


# ----------------------------------------------------------
# 2) Definisi class QueueBengkel berbasis Linked List
#    - front: node paling depan (dilayani lebih dulu / FIFO)
#    - rear : node paling belakang (tempat masuk data baru)
# ----------------------------------------------------------
class QueueBengkel:
    def __init__(self):
        self.front = None  # antrian awalnya kosong
        self.rear  = None

    def is_empty(self):
        # Antrian kosong jika front = None
        return self.front is None

    def enqueue(self, no, nama, servis):
        # --------------------------------------------------
        # Enqueue: menambah pelanggan baru ke BELAKANG antrian (rear)
        # --------------------------------------------------
        # 1) Buat node baru dengan data pelanggan
        node_baru = Node(no, nama, servis)

        # 2) Jika antrian kosong, front dan rear menunjuk node yang sama
        if self.is_empty():
            self.front = node_baru
            self.rear  = node_baru
            print(f"Pelanggan '{nama}' berhasil ditambahkan ke antrian.")
            return

        # 3) Jika antrian tidak kosong:
        #    rear lama menunjuk node baru, lalu rear berpindah ke node baru
        self.rear.next = node_baru
        self.rear = node_baru
        print(f"Pelanggan '{nama}' berhasil ditambahkan ke antrian.")

    def dequeue(self):
        # --------------------------------------------------
        # Dequeue: melayani dan menghapus pelanggan TERDEPAN (front)
        # Sesuai prinsip FIFO: yang pertama masuk, pertama dilayani
        # --------------------------------------------------
        if self.is_empty():
            print("Antrian kosong. Tidak ada pelanggan yang bisa dilayani.")
            return

        # 1) Ambil data pelanggan di posisi front
        pelanggan = self.front

        # 2) Geser front ke node berikutnya
        self.front = self.front.next

        # 3) Jika setelah geser front menjadi None, berarti antrian kosong
        #    sehingga rear juga harus diset None
        if self.front is None:
            self.rear = None

        # Tampilkan informasi pelanggan yang sedang dilayani
        print(f"\nMelayani Pelanggan:")
        print(f"  No Antrian : {pelanggan.no}")
        print(f"  Nama       : {pelanggan.nama}")
        print(f"  Servis     : {pelanggan.servis}")

    def tampilkan(self):
        # --------------------------------------------------
        # Traversal: menampilkan seluruh data antrian dari front ke rear
        # --------------------------------------------------
        if self.is_empty():
            print("Antrian kosong.")
            return

        print("\nDaftar Antrian Pelanggan Bengkel (Front -> Rear):")
        print("-" * 45)
        print(f"{'No':^6} | {'Nama':<20} | {'Servis':<15}")
        print("-" * 45)

        current = self.front  # mulai traversal dari node paling depan
        while current is not None:
            print(f"{current.no:^6} | {current.nama:<20} | {current.servis:<15}")
            current = current.next  # pindah ke node berikutnya
        print("-" * 45)


# ----------------------------------------------------------
# 3) Program Utama: Menu Interaktif Sistem Antrian Bengkel
# ----------------------------------------------------------
def main():
    # Membuat objek antrian bengkel
    q = QueueBengkel()

    # Perulangan menu utama hingga pengguna memilih keluar
    while True:
        print("\n=== Sistem Antrian Bengkel ===")
        print("1. Tambah Pelanggan")
        print("2. Layani Pelanggan")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            # Meminta input data pelanggan baru
            no     = input("No Antrian : ")
            nama   = input("Nama       : ")
            servis = input("Servis     : ")
            # Menambahkan pelanggan ke belakang antrian (enqueue)
            q.enqueue(no, nama, servis)

        elif pilih == "2":
            # Melayani pelanggan terdepan (dequeue) sesuai prinsip FIFO
            q.dequeue()

        elif pilih == "3":
            # Menampilkan seluruh isi antrian
            q.tampilkan()

        elif pilih == "4":
            # Keluar dari program
            print("Program selesai. Terima kasih!")
            break

        else:
            # Menangani input menu yang tidak valid
            print("Pilihan tidak valid")


# ----------------------------------------------------------
# 4) Penanda eksekusi file utama
# ----------------------------------------------------------
if __name__ == "__main__":
    main()
