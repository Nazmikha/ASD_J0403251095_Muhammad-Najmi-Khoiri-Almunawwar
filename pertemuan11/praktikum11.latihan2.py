# =============================================================
# Nama    : Muhammad Najmi Khoiri Almunawwar
# NIM     : J0430251095
# Kelas   : TPL - P2
# Latihan 1 - Studi Kasus DFS
# =============================================================

# Representasi graph sebagai adjacency list
# Setiap key adalah node, value adalah daftar tetangga yang terhubung langsung
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def dfs(graph, node, visited):
    """
    Fungsi penelusuran graph menggunakan Depth-First Search (DFS) secara rekursif.
    DFS masuk sedalam mungkin ke satu jalur sebelum berbalik (backtrack)
    dan mencoba jalur lain. Menggunakan prinsip Stack / rekursi (LIFO).

    Parameter:
    - graph   : dictionary adjacency list yang merepresentasikan graph
    - node    : node yang sedang dikunjungi saat ini
    - visited : set berisi node-node yang sudah pernah dikunjungi
    """

    # Tandai node saat ini sebagai sudah dikunjungi agar tidak diproses ulang
    visited.add(node)

    # Tampilkan node yang sedang dikunjungi
    print(node, end=" ")

    # Periksa semua tetangga dari node saat ini satu per satu
    for neighbor in graph[node]:
        # Hanya lanjutkan DFS ke tetangga yang belum dikunjungi
        if neighbor not in visited:
            # Panggil DFS secara rekursif — masuk lebih dalam ke jalur ini
            dfs(graph, neighbor, visited)
            # Setelah rekursi selesai (backtrack), lanjut ke tetangga berikutnya

# Set kosong untuk mencatat node yang sudah dikunjungi
visited = set()

# Jalankan DFS mulai dari node 'A'
print("DFS dari A:")
dfs(graph, 'A', visited)
print()  # Newline setelah output

# Tampilkan urutan kunjungan untuk perbandingan dengan BFS
print("\nPenjelasan urutan DFS: A -> B -> D -> E -> C -> F")
print("DFS masuk ke B dulu (tetangga pertama A), lalu ke D (terdalam di jalur B),")
print("backtrack ke B, lanjut ke E, backtrack ke A, lanjut ke C, kemudian F.")

# =============================================================
# PERBANDINGAN DFS vs BFS pada graph yang sama
# =============================================================
from collections import deque

def bfs(graph, start):
    """BFS untuk perbandingan dengan DFS pada graph yang sama."""
    visited_bfs = set()
    queue = deque([start])
    visited_bfs.add(start)
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited_bfs:
                visited_bfs.add(neighbor)
                queue.append(neighbor)

print("\n--- Perbandingan pada graph yang sama ---")
print("DFS dari A:", end=" ")
dfs(graph, 'A', set())
print()
print("BFS dari A:", end=" ")
bfs(graph, 'A')
print()

# =============================================================
# JAWABAN PERTANYAAN ANALISIS
# =============================================================

# 1. Mengapa DFS masuk ke node terdalam terlebih dahulu?
#    DFS menggunakan rekursi (atau Stack dengan prinsip LIFO — Last In First Out).
#    Ketika DFS menemukan tetangga yang belum dikunjungi, ia langsung memanggil
#    dirinya sendiri secara rekursif untuk masuk ke tetangga itu sebelum
#    memeriksa tetangga lain di level yang sama. Akibatnya, DFS terus
#    menelusuri satu jalur sampai mentok (tidak ada tetangga baru),
#    baru kemudian backtrack ke node sebelumnya dan mencoba jalur lain.
#    Contoh: dari A, DFS pilih B -> lalu pilih D (terdalam) -> D tidak punya
#    tetangga, backtrack ke B -> pilih E -> backtrack ke A -> pilih C -> F.

# 2. Apa yang terjadi jika urutan neighbor diubah?
#    Jika urutan neighbor dalam adjacency list diubah, jalur yang ditelusuri
#    DFS akan berbeda karena DFS selalu memilih tetangga pertama dalam list.
#    Contoh: jika 'A': ['C', 'B'] (C duluan), maka DFS akan mengunjungi
#    C -> F terlebih dahulu, baru kemudian B -> D -> E.
#    Urutan output: A -> C -> F -> B -> D -> E
#    Semua node tetap dikunjungi, hanya urutannya yang berbeda.

# 3. Bandingkan hasil DFS dengan BFS pada graph yang sama:
#    DFS dari A : A -> B -> D -> E -> C -> F
#    BFS dari A : A -> B -> C -> D -> E -> F
#
#    Perbedaan utama:
#    - DFS menelusuri SATU JALUR sedalam mungkin dulu (B sampai habis, baru C).
#      Cocok untuk eksplorasi jalur, backtracking, dan deteksi siklus.
#    - BFS menelusuri SEMUA NODE SATU LEVEL dulu (B dan C sebelum D, E, F).
#      Cocok untuk mencari jalur terpendek (jumlah langkah minimum).
#
#    Struktur data yang digunakan:
#    - DFS : Stack / Rekursi (LIFO)
#    - BFS : Queue / deque (FIFO)
