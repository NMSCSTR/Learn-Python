class Animal:
    def speak(self):
        print("Animal can make sound")

class Dog(Animal):
    def speak(self):
        print("Dog can bark!")

class Cat(Animal):
    def speak(self):
        print("Meow meow")

def make_sound(animal):
    animal.speak()
# Intantiate
dog = Dog()
cat = Cat()

make_sound(dog)
make_sound(cat)
    

