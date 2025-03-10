class Student: 
    def __init__(self, name, gender, age, address):
        self.name = name #ADELINE
        self.gender = gender #FEMALE
        self.age = age #18
        self.address = address #LANAO

    def get_details(self): #Getters
        print(f"Name: {self.name} Gender: {self.gender}")

# Create an objects
student1 = Student("ADELINE", "FEMALE", 18, "LANAO") 
student2 = Student("BOBORDS", "FEMALE", 18, "NAMIK") 
print(student1.name) #Output: ADELINE
student1.get_details() #Output: Name: ADELINE

# Student
# Initializations
# Methods kung CLASS function
# Objects
