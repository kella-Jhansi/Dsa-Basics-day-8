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
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def delete_at_end(self):
        if self.head is None:
            print("List is already empty.")
            return None
        if self.head.next is None:
            deleted_data = self.head.data
            self.head = None
            return deleted_data
        temp = self.head
        while temp.next:
            temp = temp.next
        deleted_data = temp.data
        temp.prev.next = None
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

# Main Execution
dll = DoublyLinkedList()

# Insert elements at beginning
n = int(input("Enter the number of elements to insert at beginning: "))
for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    dll.insert_at_beginning(val)

print("\nOriginal List:")
dll.display()

# Delete elements from end
delete_count = int(input("\nEnter how many nodes to delete from end: "))
actual_deleted = 0
for _ in range(delete_count):
    deleted = dll.delete_at_end()
    if deleted is not None:
        print(f"Deleted node with value: {deleted}")
        actual_deleted += 1
    else:
        print("No more nodes to delete.")
        break

print(f"\nTotal nodes deleted: {actual_deleted}")
print("Remaining list:")
dll.display()
