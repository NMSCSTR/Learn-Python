def quiz():
    score = 0
    total_questions = 3

    print("📌 Python Functions Quiz\n")

    # Question 1: Function with Parameters
    print("1️⃣ What will be the output of the following function?")
    print("""
def multiply(a, b):
    return a * b

print(multiply(2, 3))
    """)
    print("A) 5")
    print("B) 6")
    print("C) Error")
    print("D) None")
    
    answer1 = input("Your answer: ").strip().upper()
    if answer1 == "B":
        print("✅ Correct!\n")
        score += 1
    else:
        print("❌ Incorrect. The correct answer is B) 6\n")

    # Question 2: Function with Default Parameters
    print("2️⃣ What will be printed when calling `greet()`?")
    print("""
def greet(name="Student"):
    print("Hello,", name)

greet()
    """)
    print("A) Hello, Student")
    print("B) Hello, ")
    print("C) Error")
    print("D) None")
    
    answer2 = input("Your answer: ").strip().upper()
    if answer2 == "A":
        print("✅ Correct!\n")
        score += 1
    else:
        print("❌ Incorrect. The correct answer is A) Hello, Student\n")

    # Question 3: Functions with Multiple Return Values
    print("3️⃣ What will be the output of the following function?")
    print("""
def calculate(a, b):
    return a + b, a - b

sum_result, diff_result = calculate(10, 4)
print(sum_result, diff_result)
    """)
    print("A) 10 4")
    print("B) 6 14")
    print("C) 14 6")
    print("D) Error")
    
    answer3 = input("Your answer: ").strip().upper()
    if answer3 == "C":
        print("✅ Correct!\n")
        score += 1
    else:
        print("❌ Incorrect. The correct answer is C) 14 6\n")

    # Final Score
    print("📊 Quiz Completed!")
    print(f"Your Score: {score}/{total_questions}")

    if score == total_questions:
        print("🎉 Excellent! You got all answers correct!")
    elif score >= 2:
        print("👍 Good job! Keep practicing.")
    else:
        print("📖 Review the concepts and try again.")

# Run the quiz
quiz()
