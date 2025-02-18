marks = int(input("Enter grade \n"))

if marks >= 99:
    grade = "Excellent"
elif marks >= 90:
    grade = "A++"
else:
    grade ="Fail"

print(grade)