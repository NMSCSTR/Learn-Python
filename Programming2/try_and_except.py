


# Defining a custom exception by creating a class that inherits from Exception
class NegativeNumberError(Exception):
    pass  # 'pass' means this class inherits everything from Exception without adding anything new

try:
    num = int(input("Enter a positive number: "))  # Accepting input from the user
    if num < 0:  # Checking if the number is negative
        raise NegativeNumberError("Negative numbers are not allowed.")  # Raising custom exception
    print("Valid number:", num)  # Printing the valid number if no error occurs
except NegativeNumberError as e:  # Catching the custom exception
    print(e)  # Printing the custom error message
