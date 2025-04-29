class Candidate:
    def __init__(self, name, age, position):
        self.name = name #BBM
        self.age = age #56
        self.position = position #Mayor

    def introduce(self): #BBM       #56
        print(f"I am {self.name}, {self.age} years old, running for {self.position}")
        #Mayor
    
# Sub Class(child) 
class MayorCandidate(Candidate):
    def __init__(self, name, age, position, city):
        super().__init__(name, age, position) #Attr from parent class
        self.city = city # Tangub City

    def introduce(self):
        super().introduce() #from the base class
        print(f"My goal is to improve {self.city}")
                                      #Tangub City

class PresidentCandidate(Candidate):
    def __init__(self, name, age, position, vision):
        super().__init__(name, age, position)
        self.vision = vision

    def introduce(self):
        super().introduce()
        print(f"{self.vision}")
# Create object for Mayor Candidate
Mayor1 = MayorCandidate("Digong",56,"Mayor","Tangub City")
Mayor1.introduce()
President1 = PresidentCandidate("BBM",45,"President","My vision is to improve drug production and best quality in the Philippines")
President1.introduce()