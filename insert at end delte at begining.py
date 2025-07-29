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
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def delete_at_beginning(self):
        if self.head is None:
            return None  # Empty list
        deleted_data = self.head.data
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        return deleted_data

    def display(self):
        temp = self.head
        if not temp:
            print("List is empty.")
            return
        while temp:
            print(temp.data, end=" <=> ")
            temp = temp.next
        print("None")

# Main execution
dll = DoublyLinkedList()

# Insert elements at end
n = int(input("Enter the number of elements to insert at end: "))
for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    dll.insert_at_end(val)

print("\nOriginal List:")
dll.display()

# Delete elements from beginning
delete_count = int(input("\nEnter how many nodes to delete from beginning: "))
actual_deleted = 0
for _ in range(delete_count):
    deleted = dll.delete_at_beginning()
    if deleted is not None:
        actual_deleted += 1
    else:
        break  # List became empty

print(f"\nDeleted first {actual_deleted} node(s).")
print("Remaining elements:")
dll.display()
