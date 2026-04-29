#=================================================
# Nama : Muhammad Tauriq Arya Pradita
# NIM  : J0403251149
# KELAS: KELAS B
#=================================================
# Materi 3 : Implementasi DFS
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


def dfs(graph,node,visited):
    #fungsi untuk melakukan penelusuran graph dengan DFS
    # graph : dictionary yang menyimoan struktur dari graph
    #node : menyimpan node yang sedang dikunjungi
    #visited : menyimpan node yang sudah dikunjungi

    #tandai node saat ini sebagai node yang sudah dikunjungi
    visited.add(node)

    #tampilkan node yang sedang dikunjungi
    print(node, end=" ")

    #periksa semua tetangga dari node saat ini
    for neighbor in graph[node]:

        #jika tetangga belum pernah dikunjungi
        if neighbor not in visited:
            #lakukan DFS secara rekursif tentangga tersebut
            dfs(graph,neighbor,visited)

#set visited
visited = set()

#menjalankan DFS dari A
dfs(graph,"A",visited)