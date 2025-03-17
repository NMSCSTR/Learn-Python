class Car:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    # Getter methods
    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_price(self):
        return self.price

    # Setter method
    def set_price(self, new_price):
        self.price = new_price

    # Method to display car details
    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Price: ${self.price}")

    # Method to check affordability (returns boolean only)
    def is_affordable(self, budget):
        return self.price <= budget


# Creating car objects
car1 = Car("Toyota", "Camry", 2020, 25000)
car2 = Car("Honda", "Civic", 2019, 22000)
car3 = Car("BMW", "X5", 2021, 60000)

# Displaying car details
car1.display_info()
car2.display_info()
car3.display_info()

# Modifying the price of car2
car2.set_price(21000)
print("\nAfter modifying car2's price:")
car2.display_info()

# Checking affordability (boolean only)
budget = 30000
print(f"\nIs car1 affordable? {car1.is_affordable(budget)}")
print(f"Is car3 affordable? {car3.is_affordable(budget)}")
