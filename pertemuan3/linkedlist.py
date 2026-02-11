#=================================================================
#Single	Linkedlist	dasar	pada	pyhthon :
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None #Tambahan tail untuk menunjuk ke node terakhir
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node # Inisialisasi tail pada node pertama
        else:
            self.tail.next = new_node # Hubungkan node terakhir dengan node baru
            self.tail = new_node # Perbarui tail ke node baru

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

# CONTOH PENGGUNAAN
ll = LinkedList()
ll.insert_at_end(5)
ll.insert_at_end(5)
ll.insert_at_end(13)
ll.insert_at_end(2)
ll.display()
#=================================================================
# Double Linkedlist dasar pada python :
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None # Menyimpan node terakhir untuk traversing mundur
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
        print("\nTraversing forward:")
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
            print("null")
    def display_backward(self):
        print("\nTraversing backward:")
        temp = self.tail
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.prev
            print("null")
    
    def delete_node(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
            if temp is None:
                return
            prev.next = temp.next
            temp = None
            
# Contoh Penggunaan
dll = DoublyLinkedList()
dll.insert_at_end(3)
dll.insert_at_end(5)
dll.insert_at_end(13)
dll.insert_at_end(2)
dll.delete_node(5)
dll.display_forward()
dll.display_backward()

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
        print("\nTraversing forward:")
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    def display_backward(self):
        print("\nTraversing backward:")
        temp = self.tail
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.prev
        print("null")

    def delete_node(self, key):
        temp = self.head

        while temp:
            if temp.data == key:

                # Jika node adalah head
                if temp == self.head:
                    self.head = temp.next
                    if self.head:
                        self.head.prev = None
                    else:
                        self.tail = None

                # Jika node adalah tail
                elif temp == self.tail:
                    self.tail = temp.prev
                    self.tail.next = None

                # Jika node di tengah
                else:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev

                return  # keluar setelah delete

            temp = temp.next

dll = DoublyLinkedList()
dll.insert_at_end(3)
dll.insert_at_end(5)
dll.insert_at_end(13)
dll.insert_at_end(2)

dll.delete_node(5)

dll.display_forward()
dll.display_backward()