class Node:
    def __init__(self, data):
        self.data = data  # Store the data
        self.prev = None  # Pointer to the previous node
        self.next = None  # Pointer to the next node

node1 = Node(10)
node2 = Node(20)
node1.next = node2

print(node1.next.data)
print(node2.prev.data)