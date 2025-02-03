
#Is The Triangle Equilateral? Activity
# x = int(input("Enter x: "))
# y = int(input("Enter y: "))
# z = int(input("Enter z: "))

# if x == y and y == z:
#     print("Triangle is equilateral.")

# Same Sign Activity

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if (num1 > 0 and num2 > 0) or (num1 < 0 and num2 < 0):
    print("Numbers have the same sign.")


""" Write a program that takes three integers, num1, num2, and num3, as input and check if all three numbers are equal. If all numbers are equal, print "All numbers are equal." Otherwise, print "Not all numbers are equal. """
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

result = num1 == num2 == num3

if result:
    print("All numbers are equal.")
else:
    print("Not all numbers are equal.")