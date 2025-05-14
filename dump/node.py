class Person:
    def __init__(self, name, age):
        self.name = name      
        self.age = age

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        if age > 0:
            self.age = age
        else:
            print("Age must be positive.")

    def describe(self):
        print(f"{self.name} is {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def describe(self):
        print(f"Student {self.get_name()} (ID: {self.student_id}) is {self.get_age()} years old.")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def describe(self):
        print(f"Teacher {self.get_name()} teaches {self.subject} and is {self.get_age()} years old.")

student1 = Student("Alice", 18, "S12345")
teacher1 = Teacher("Mr. Kingkong", 35, "Programming")

student1.describe()
teacher1.describe()

print("\nUpdating Student's age...")
student1.set_age(19)
teacher1.set_age(20)
print(f"{student1.get_name()}'s new age is {student1.get_age()}.")
print(f"{teacher1.get_name()}'s new age is {teacher1.get_age()}.")

print("\nUpdating Student's name...")
student1.set_name("Luna")
teacher1.set_name("Mr. Rodolf")
print(f"Student's new name is {student1.get_name()}, {student1.get_name()}'s new age is {student1.get_age()}.")
print(f"Teacher's new name is {teacher1.get_name()}, {teacher1.get_name()}'s new age is {teacher1.get_age()}.")

print("\n")
student1.describe()
teacher1.describe()