
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None




            
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


ll.display()
