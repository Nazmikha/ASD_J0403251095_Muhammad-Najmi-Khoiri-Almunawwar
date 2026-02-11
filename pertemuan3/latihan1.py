# MUHAMMAD NAJMI KHOIRI ALMUNAWWAR 
# NIM J0403251095 (Ganjil)
#=============================================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
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
            self.tail = new_node

    def delete_node(self, key):
        temp = self.head

        if not temp:
            return

        if temp.data == key:
            self.head = temp.next
            if self.head is None:
                self.tail = None
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next

        if temp == self.tail:
            self.tail = prev

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")


# Test
ll = LinkedList()
data_input = input("Masukkan elemen-elemen untuk Double Linked List (pisahkan dengan spasi): ")
data_list = data_input.split()
for data in data_list:
    ll.insert_at_end(int(data))


ll.delete_node(int(input("Masukkan elemen yang ingin dihapus: ")))

ll.display()
# =============================================