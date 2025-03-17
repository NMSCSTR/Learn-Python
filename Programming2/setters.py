class Student:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname # Pagobo 

    def get_firstname(self):
        print(f"Firstname: {self.firstname}")
    def get_lastname(self):
        print(f"Lastname: {self.lastname}")

    def set_lastname(self, newLastname):
        self.lastname = newLastname #Duterte
    


s1 = Student("Rhondel", "Pagobo")
s2 = Student("Archie", "Catalan")

s1.get_firstname()
s1.get_lastname()
print()
s2.get_firstname()
s2.get_lastname()

s1.set_lastname("Duterte")

print("After modifying")
s1.get_firstname()
s1.get_lastname()
