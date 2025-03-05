class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def new_line(self):
        print("--------------------")

    def get_car_info(self):
        print(f"This {self.brand} {self.model} was invented at {self.year}")

    def set_brand(self, brand):
        self.brand = brand

    def set_model(self, model):
        self.model = model

# Creating an object
car1 = Car("Honda", "Civic", 2007) #Creating an object
car2 = Car("Toyota", "Mk5 Supra", 2009) #Creating an object
car1.set_brand("Nissan") #Changing the brand of the car
car1.set_model("Skyline") #Changing the model of the car

#Accesing info using method inside the class
car1.get_car_info()
car1.new_line()
car2.get_car_info()

