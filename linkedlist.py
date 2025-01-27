class Node:
    """A node in the linked list."""
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Pointer to the next node

class LinkedList:
    """A singly linked list."""
    def __init__(self):
        self.head = None  # Initialize the head of the list

    def append(self, data):
        """Add a node to the end of the linked list."""
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Traverse to the end of the list
                current = current.next
            current.next = new_node

    def display(self):
        """Print all elements in the linked list."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete(self, data):
        """Delete the first occurrence of a node with the given data."""
        if not self.head:  # If the list is empty
            print("List is empty.")
            return

        # If the head node is the one to be deleted
        if self.head.data == data:
            self.head = self.head.next
            return

        # Traverse the list to find the node to delete
        current = self.head
        while current.next and current.next.data != data:
            current = current.next

        if current.next:  # Node to delete is found
            current.next = current.next.next
        else:
            print("Data not found in the list.")

# Example Usage
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.display()  # Output: 10 -> 20 -> 30 -> None
linked_list.delete(20)
linked_list.display()  # Output: 10 -> 30 -> None
