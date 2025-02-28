import pdb  # Importing the built-in Python debugger module

def calculate(num):
    pdb.set_trace()  # Starting the debugger at this point
    result = 10 / num  # Calculating the division
    return result  # Returning the result

try:
    number = int(input("Enter a number: "))  # Taking input from user
    print(calculate(number))  # Calling the function and printing the result
except ZeroDivisionError:  # Catching ZeroDivisionError
    print("Cannot divide by zero.")
