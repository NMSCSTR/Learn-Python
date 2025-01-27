class Node:
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Pointer to the next node

node1 = Node(10)
node2 = Node(20)
node1.next = node2  # Linking node1 to node2
print(node1.data)  # Output: 10
print(node1.next.data)  # Output: 20
