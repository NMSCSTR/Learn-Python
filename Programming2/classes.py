class Patient:
    def __init__(self, name, age, patient_id, disease):
        self.name = name
        self.age = age
        self.patient_id = patient_id
        self.disease = disease

    # Getter methods
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_patient_id(self):
        return self.patient_id

    def get_disease(self):
        return self.disease

    # Setter method
    def set_disease(self, new_disease):
        self.disease = new_disease

    # Method to check if patient is a senior citizen
    def is_senior(self):
        return self.age >= 65

    # Method to display patient details
    def display_info(self):
        print(f"Patient Name: {self.name}, Age: {self.age}, ID: {self.patient_id}, Disease: {self.disease}")


# Creating patient objects
patient1 = Patient("Alice", 70, 101, "Diabetes")
patient2 = Patient("Bob", 45, 102, "Flu")
patient3 = Patient("Charlie", 67, 103, "Heart Disease")

# Displaying details
patient1.display_info()
patient2.display_info()
patient3.display_info()
print()
print()
print()
print(patient1.get_name())
print()
print()
print()
# Modifying disease
patient2.set_disease("Pneumonia")

# Checking senior status
print(f"Is {patient1.get_name()} a senior? {patient1.is_senior()}")  # Output: True
print(f"Is {patient2.get_name()} a senior? {patient2.is_senior()}")  # Output: False
print(f"Is {patient3.get_name()} a senior? {patient3.is_senior()}")  # Output: True
