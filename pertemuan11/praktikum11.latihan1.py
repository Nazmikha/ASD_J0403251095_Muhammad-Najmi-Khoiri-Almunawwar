# =============================================================
# Nama    : Muhammad Najmi Khoiri Almunawwar
# NIM     : J0430251095
# Kelas   : TPL - P2
# Latihan 1 - Studi Kasus BFS (Jalur Terdekat Lokasi)
# =============================================================

from collections import deque

# Representasi graph sebagai adjacency list
# Setiap key adalah lokasi, value adalah daftar lokasi yang bisa dicapai langsung
graph = {
    'Rumah': ['Sekolah', 'Toko'],
    'Sekolah': ['Perpustakaan'],
    'Toko': ['Pasar'],
    'Perpustakaan': [],
    'Pasar': []
}

def bfs(graph, start):
    """
    Fungsi penelusuran graph menggunakan Breadth-First Search (BFS).
    BFS mengunjungi node secara melebar (level per level) menggunakan Queue (FIFO).

    Parameter:
    - graph : dictionary adjacency list yang merepresentasikan graph
    - start : node awal penelusuran
    """

    # Set untuk mencatat node yang sudah dikunjungi agar tidak diproses ulang
    visited = set()

    # Queue (deque) menyimpan node yang akan diproses, dimulai dari node awal
    queue = deque([start])

    # Tandai node awal sebagai sudah dikunjungi sebelum masuk ke loop
    visited.add(start)

    # Proses terus berjalan selama queue tidak kosong
    while queue:
        # Ambil node paling depan dari queue (prinsip FIFO)
        node = queue.popleft()

        # Tampilkan node yang sedang dikunjungi
        print(node, end=" ")

        # Periksa semua tetangga dari node saat ini
        for neighbor in graph[node]:
            # Hanya proses tetangga yang belum pernah dikunjungi
            if neighbor not in visited:
                visited.add(neighbor)       # Tandai sebagai sudah dikunjungi
                queue.append(neighbor)      # Masukkan ke queue untuk diproses nanti

# Jalankan BFS mulai dari node 'Rumah'
print("BFS dari Rumah:")
bfs(graph, 'Rumah')
print()  # Newline setelah output

# =============================================================
# JAWABAN PERTANYAAN ANALISIS
# =============================================================

# 1. Node mana yang dikunjungi pertama?
#    Node pertama yang dikunjungi adalah 'Rumah', karena 'Rumah' adalah
#    node awal (start) yang dimasukkan ke queue pertama kali.
#    Setelah Rumah, urutan kunjungan adalah: Rumah -> Sekolah -> Toko -> Perpustakaan -> Pasar
#    BFS mengunjungi Sekolah dan Toko terlebih dahulu (level 1 dari Rumah)
#    sebelum lanjut ke Perpustakaan dan Pasar (level 2).

# 2. Mengapa BFS cocok untuk mencari jalur terdekat?
#    BFS menelusuri graph secara melebar level per level menggunakan Queue (FIFO).
#    Artinya, node-node yang jaraknya 1 langkah dari start diproses dahulu,
#    baru kemudian node yang jaraknya 2 langkah, dan seterusnya.
#    Karena itu, node tujuan pasti ditemukan melalui jalur dengan jumlah
#    edge (hop) paling sedikit — itulah jalur terdekat pada graph tak berbobot.
#    Contoh: untuk mencapai Perpustakaan, BFS menemukan jalur Rumah->Sekolah->Perpustakaan
#    (2 langkah) tanpa pernah mencoba jalur yang lebih panjang terlebih dahulu.

# 3. Apa perbedaan urutan BFS jika struktur graph diubah?
#    Urutan BFS sangat bergantung pada struktur adjacency list graph.
#    Jika urutan tetangga dalam list diubah, urutan kunjungan pada level yang
#    sama akan berubah. Misalnya, jika graph diubah menjadi:
#    'Rumah': ['Toko', 'Sekolah']  (urutan dibalik)
#    maka hasil BFS menjadi: Rumah -> Toko -> Sekolah -> Pasar -> Perpustakaan
#    Selain itu, jika koneksi antar node ditambah atau dihapus, level-level
#    dalam BFS juga akan berubah sehingga urutan kunjungan ikut berubah.
