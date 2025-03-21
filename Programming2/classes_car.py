class Patient:
    def __init__(self, name, age, patient_id, disease):
        self.name = name #Stored object called name
        self.age = age #Stored object called age
        self.patient_id = patient_id #Stored object called patient_id
        self.disease = disease #Stored object called disease

    # Getters
    def get_name(self):
        return self.name # John
    def get_age(self):
        return self.age # 29
    def get_patient_id(self):
        return self.patient_id #111
    def get_disease(self):
        return self.disease #Heartache
    
    # Setters
    def set_disease(self, new_disease):
        self.disease = new_disease
    
# Creating 3 objects
p1 = Patient("John", 29, 111, "Heartache")
p2 = Patient("Jane", 65, 112, "Cough")
p3 = Patient("Jessy", 20, 113, "Kalibanga")

print("Name: ", p1.get_name())
print("Age: ", p1.get_age())
print("Patient Id: ",p1.get_patient_id())
print("Disease: ", p1.get_disease())
print() #Generate new line
print("Name: ", p2.get_name())
print("Age: ", p2.get_age())
print("Patient Id: ",p2.get_patient_id())
print("Disease: ", p2.get_disease())
print() #Generate new line
 # Used the setters(update)
print("Name: ", p3.get_name())
print("Age: ", p3.get_age())
print("Patient Id: ",p3.get_patient_id())
print("Disease: ", p3.get_disease())
p3.set_disease("Hubak")

class Patient:
    def __init__(self, name, age, patient_id, disease):
        self.name = name #Stored object called name
        self.age = age #Stored object called age
        self.patient_id = patient_id #Stored object called patient_id
        self.disease = disease #Stored object called disease

    # Getters
    def get_name(self):
        return self.name # John
    def get_age(self):
        return self.age # 29
    def get_patient_id(self):
        return self.patient_id #111
    def get_disease(self):
        return self.disease #Heartache
    
    # Setters
    def set_disease(self, new_disease):
        self.disease = new_disease
    
# Creating 3 objects
p1 = Patient("John", 29, 111, "Heartache")
p2 = Patient("Jane", 65, 112, "Cough")
p3 = Patient("Jessy", 20, 113, "Kalibanga")

print("Name: ", p1.get_name())
print("Age: ", p1.get_age())
print("Patient Id: ",p1.get_patient_id())
print("Disease: ", p1.get_disease())
print() #Generate new line
print("Name: ", p2.get_name())
print("Age: ", p2.get_age())
print("Patient Id: ",p2.get_patient_id())
print("Disease: ", p2.get_disease())
print() #Generate new line
 # Used the setters(update)
print("Name: ", p3.get_name())
print("Age: ", p3.get_age())
print("Patient Id: ",p3.get_patient_id())
print("Disease: ", p3.get_disease())
p3.set_disease("Hubak")