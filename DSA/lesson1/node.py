class BookNode:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.next = None

book1 = BookNode("Harry Potter", "J.K. Rowling")
book2 = BookNode("The Hobbit", "J.R.R Toklin")
book3 = BookNode("1984", "George Orweel")

book1.next = book2
book2.next = book3

current = book1
while current:
    print(f"Title: {current.title}, Author: {current.author}")
    current = current.next
print("End of the list")