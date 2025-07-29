class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node  # fixed typo here
        self.head = new_node

    def display(self):
        temp = self.head
        print("Doubly Linked List (Forward):")
        while temp:
            print(temp.data, end=" <=> ")
            temp = temp.next
        print("None")

    def backtraverse(self):
        print("Doubly Linked List (Backward):")
        temp = self.head
        if not temp:
            print("Empty list")
            return
        # Go to the last node
        while temp.next:
            temp = temp.next
        # Traverse backwards
        while temp:
            print(temp.data, end=" <=> ")
            temp = temp.prev
        print("None")

# Main execution
dll = DoublyLinkedList()
n = int(input("Enter the number of elements to insert at beginning: "))
for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    dll.insert_at_beginning(val)

dll.display()
dll.backtraverse()

