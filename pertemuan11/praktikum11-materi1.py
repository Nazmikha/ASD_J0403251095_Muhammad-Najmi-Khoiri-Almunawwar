#=================================================
# Nama : Muhammad Tauriq Arya Pradita
# NIM  : J0403251149
# KELAS: KELAS B
#=================================================
# Materi 1 : Implementasi Dasar Graph
#=================================================

graph = {
    'A' : ['B','C'],
    'B' : ['A','D'],
    'C' : ['A','D'],
    'D' : ['B','C']
}

for node in graph :
    print(node, '->', graph[node])