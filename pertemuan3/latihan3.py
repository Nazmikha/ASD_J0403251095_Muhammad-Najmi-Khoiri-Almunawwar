class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def display_forward(self):
        print("\nTampilan Maju:")
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    def display_backward(self):
        print("\nTampilan Mundur:")
        temp = self.tail
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.prev
        print("null")
    

    def search(self, key):
        # Jika list kosong
        if self.head is None:
            print("Tidak ada data yang bisa dicari")
            return False

        temp = self.head
        position = 0

        while temp:
            if temp.data == key:
                print(f"Data {key} ditemukan pada posisi ke-{position}")
                return True
            temp = temp.next
            position += 1

        print(f"Data {key} tidak ditemukan")
        return False



dll = DoublyLinkedList()
data_input = input("Masukkan elemen-elemen untuk Double Linked List (pisahkan dengan spasi): ")
data_list = data_input.split()
for data in data_list:
    dll.insert_at_end(int(data))

dll.display_forward()
dll.display_backward()
key = int(input("Masukkan elemen yang ingin dicari: "))
dll.search(key)




