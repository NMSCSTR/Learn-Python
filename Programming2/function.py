# Function with no parameter
def greet():
    print("Hello, welcome to function")

greet() # Function call

print("\n")

# Function with parameters
def add(a, b):
    return a + b
result = add(5, 3)
print("Sum:", result)

print("\n")

# Function with default parameters
def greet_user(name="Rhondel"):
    print(f"hello, {name}!")

greet_user()


# Functions With Multiple Return Values
def get_square_and_cube(n):
    return n ** 2, n**3
square, cube = get_square_and_cube(3)
print("Sqaure: ", square, "Cube: ", cube)