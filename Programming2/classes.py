class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    # Getters
    def get_title(self):
        print(f"Title: {self.title}")

    def get_author(self):
        print(f"Author: {self.author}")

    def get_year(self):
        print(f"Year: {self.year}")
    # Setters
    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author

    def set_year(self, year):
        self.year = year # New value or object

book1 = Book("Alice in the wonderland" , "Alegrado", 2008)
book2 = Book("Ben10" , "Kirou", 2001)

# Getters
book1.get_title()
book2.get_title()
print()
book1.get_author()
book2.get_author()
print()
book1.get_year()
book2.get_year()
print("SETTERS")
# Setters
book1.set_title("Super Book")
book1.get_title()



# Tommorow
# CAñAS, JUSTIN CEDRIC
# TAN, CJ
# ECDANG, CITO JOHN
# CARTAJENAS, JHOPERSIE
# MANLEGRO, MARK DALE
# FLORIDA, KIROU
# ALEGRADO, VENZ CARLO
# BUGAS, GWENA
# CABASAN, ALDRIN
# ASISTER, MELCHIE
# ALAMAG, LJ MAE
# ENOMAR, CAMILE

# Friday
# PAMA, CHARLENE
# ABELILLA, DARYN RHAEL
# PENOLIAD, MARVIE JR.
# CODANTE, AMINODEN kyuttie
# CALIAO, KHALEL JHON
# TAYROS, DANMER
# ARMADA, MARK DANIEL
# MANCAO, AILYN
# LAPITAN, KIERTENE FAITH
# MATIN-AO, REYGIE
# BAOY, JAMES BRYAN