
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

        
        
    def append (self,data):
        new_node = Node(data)

        if not self.head:
             self.head = new_node 

        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node


    def delete(self):
        if not self.head:
            print("List is Empty")
        elif not self.head.next:
            self.head = None
        else:
            current = self.head
            while current.next.next:
                current = current.next
            current.next = None

            
    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("None")

ll = LinkedList() 

ll.append(10)  
ll.append(20)  
ll.append(30)  
ll.append(40) 
ll.delete()

ll.display()
