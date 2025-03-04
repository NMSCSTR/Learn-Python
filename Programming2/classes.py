class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

# Create an object
car1 = Car("Honda", "Civic", 2009)
print(car1.model)