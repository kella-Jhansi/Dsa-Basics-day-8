class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

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
        # Move to the last node
        while temp.next:
            temp = temp.next
        # Traverse backward
        while temp:
            print(temp.data, end=" <=> ")
            temp = temp.prev
        print("None")

# Main execution
dll = DoublyLinkedList()
n = int(input("Enter the number of elements to insert at end: "))
for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    dll.insert_at_end(val)

dll.display()
dll.backtraverse()
