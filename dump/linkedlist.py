
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node #10
        else:
            current = self.head #10 #20
            while current.next:
                current = current.next #None
            current.next = new_node #20

    # Method to delete the last node in the linked list
    def delete(self):
        # If the list is empty, just print a message
        if not self.head:
            print("List is empty!")
        # If there's only one node, remove it by setting head to None
        elif not self.head.next:
            self.head = None
            # Traverse the list to find the second last node
        else:
            current = self.head #10
            # Stop when current.next.next is None, meaning current is second last
            while current.next.next:
                current = current.next
            # Remove the last node by setting second last node's next to None
            current.next = None

            
    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("None")

ll = LinkedList() #Intance

# Append values to the list
ll.append(10)   # List: 10
ll.append(20)   # List: 10 -> 20
ll.append(30)   # List: 10 -> 20 -> 30
ll.append(40)   # List: 10 -> 20 -> 30 -> 40
ll.delete()

# Display the current list
ll.display()     # Output: 10 -> 20 -> 30 -> 40 -> None
