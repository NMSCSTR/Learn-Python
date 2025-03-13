class Patient:
    def __init__(self, name, age, patient_id, disease):
        self.name = name
        self.age = age
        self.patient_id = patient_id
        self.disease = disease

        def get_name(name):
            print(f"The name of patient is", {self.name})
        def get_age(age):
            print(f"Age of the patient", {self.age})
        def get_patient_id(patient_id):
            print(f"Patient_id", {self.patient_id})


Patient1 = Patient("Stephen", 69, 123, "ubo")
Patient2 = Patient("Balmon", 19, 456, "kagid")
Patient3 = Patient("Bubords", 23, 789, "sipon")

Patient1.get_info