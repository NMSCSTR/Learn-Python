class Animal:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def make_sound(self):
        print("Some animal sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def make_sound(self):
        print("Woof!")

    def display_info(self):
        print(f"Name: {self.get_name()}, Breed: {self.breed}")

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def make_sound(self):
        print("Meow!")

    def display_info(self):
        print(f"Name: {self.get_name()}, Color: {self.color}")

animal = Animal("Generic Animal")
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Tabby")

print(f"Dog's name (inherited): {dog.get_name()}")
print(f"Cat's name (inherited): {cat.get_name()}")

animal.make_sound()
dog.make_sound()
cat.make_sound()

animal.set_name("Generic New Animal")
print(f"Animal's new name: {animal.get_name()}")

dog.display_info()
cat.display_info()