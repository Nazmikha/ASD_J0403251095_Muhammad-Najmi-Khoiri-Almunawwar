#=================================================
# Nama : Muhammad Tauriq Arya Pradita
# NIM  : J0403251149
# KELAS: KELAS B
#=================================================
# Materi 2 : Implementasi BFS
#=================================================

#sruktur data untuk membuat antrian, kita gunakan dari library collections bawaan python
from collections import deque

#representasi graph
graph = {
    'A' : ['B','C'],
    'B' : ['D','E'],
    'C' : ['F','G'],
    'D' : [],
    'E' : [],
    'F' : [],
    'G' : [],
}



def bfs(graph,start):
    #fungsi untuk melakukan penelusuran graph dengan BFS
    # graph : dictionary yang menyimoan struktur dari graph
    # start : node awal penelusuran

    # queue digunakan unutuk menyimpan node yang akan diproses/dibaca
    queue = deque()

    #variabel yang digunakan untuk menyimpan node yang sudah diproses/sudah dikunjungi
    visited = set()

    #masukan node awal ke queue
    queue.append(start)

    #ditandai node awal sebagai yang sudah dikunjungi
    visited.add(start)

    while queue:
        #mengambil node paling depan dari queue
        node = queue.popleft()

        #tampilkan node yang sedang dikunjungi
        print(node,end=" ")

        #periksa semua tetangga dari node yang diambil
        for neighbor in graph[node]:
            #jika tetangga sebelum dikunjungi
            if neighbor not in visited:
                #tandai sebagai sudah dikunjungi
                visited.add(neighbor)
                #masukan tetangga ke queue unutuk diproses nanti
                queue.append(neighbor)
        
#menjalankan BFS dari node A
bfs(graph,'A')
