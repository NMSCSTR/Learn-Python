# def class Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# Def class linkedlist
# # contructor initialize an empty linkedlist
class LinkedList:
    def __init__(self):
        self.head = None
#def function for appending data into linkedlist
    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
#def function for for displaying
    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("None")
#Instantiate(create object for linkedlist)
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)
linked_list.display()