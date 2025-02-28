try:
    # Try block will attempt to execute the code
    num = int(input("Enter a number: "))  # Asking user for a number input
    result = 10 / num  # Dividing 10 by the user's input
    print("Result:", result)  # Printing the result if no error occurs
except ZeroDivisionError:  # This block will execute if the user enters 0
    print("Cannot divide by zero.")  
except ValueError:  # This block will execute if the user enters non-numeric input
    print("Invalid input. Please enter a number.")
finally:
    # This block always executes whether an error occurs or not
    print("Execution Completed.")
