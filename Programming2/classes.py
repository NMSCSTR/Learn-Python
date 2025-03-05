class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def new_line(self):
        print("--------------------")

    def get_car_info(self):
        print(f"This {self.brand} {self.model} was invented at {self.year}")

# Creating an object
car1 = Car("Honda", "Civic", 2007) #Creating an object
car2 = Car("Toyota", "Mk5 Supra", 2009) #Creating an object


#Accesing info using method inside the class
car1.get_car_info()
car1.new_line()
car2.get_car_info()

