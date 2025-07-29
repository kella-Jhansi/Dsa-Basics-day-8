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

    def delete_by_value(self, value):
        if self.head is None:
            print("List is empty.")
            return False

        temp = self.head
        while temp:
            if temp.data == value:
                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    # Deleting the head node
                    self.head = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                print(f"Deleted node with value: {value}")
                return True
            temp = temp.next

        print(f"Value {value} not found in the list.")
        return False

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

# Delete by value
value_to_delete = int(input("\nEnter the value to delete: "))
dll.delete_by_value(value_to_delete)

print("\nList after deletion:")
dll.display()
