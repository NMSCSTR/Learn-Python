# Creating a  class called car
class Car:
    # Initialization with the car attributes
    def __init__(self, brand, model, year, price):
        self.brand  = brand
        self.model  = model
        self.year  = year
        self.price  = price

    # Getters
    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_price(self):
        return self.price
    
    # Setters
    def set_price(self, new_price):
        self.price = new_price

    def display_info(self):
        print(f"Car brand: {self.brand} model was {self.model} year invented {self.year} with the price of {self.price} ")

    def is_affordable(self, budget):
        return self.price <= budget

# Create and update objects
car1 = Car("Toyota","Fortuner", 2001, 200)
car2 = Car("Misyubibi","Sample", 2001, 600)
car3 = Car("Toyota","Vios", 2001, 500)

car2.set_price(400)

print(f"Can afford {car2.get_brand()}? {car2.is_affordable(300)}")




list - insert, remove, find  or search  - 2d List
function 
Class

