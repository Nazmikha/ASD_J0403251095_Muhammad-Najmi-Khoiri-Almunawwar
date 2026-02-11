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

    # Display maju
    def display_forward(self):
        if self.head is None:
            print("List kosong")
            return

        temp = self.head
        print("Linked list sebelum dibalik : ", end="")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    # Display mundur (pakai stack)
    def display_backward(self):
        if self.head is None:
            print("List kosong")
            return

        stack = []
        temp = self.head

        while temp:
            stack.append(temp.data)
            temp = temp.next

        print("Linked list sesudah dibalik : ", end="")
        while stack:
            print(stack.pop(), end=" -> ")
        print("null")

ll= LinkedList()
data_input = input("Masukkan elemen-elemen untuk Double Linked List (pisahkan dengan spasi): ")
data_list = data_input.split()
for data in data_list:
    ll.insert_at_end(int(data))
ll.display_forward()
ll.display_backward()