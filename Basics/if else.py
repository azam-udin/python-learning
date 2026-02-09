#if else statement
temperature = 25

if temperature > 30:
    print("It's a hot day")
else:
    print("It's not too hot today")

#if elif else statement
score=85

if score >= 90:
    grade = "A"
    print("Excellent!")
elif score >= 75:
    grade = "B"
    print("Well done!")
elif score >= 60:
    grade = "C"
    print("Good effort!")
else:
    grade = "F"
    print("Better luck next time!")

print(f"Your grade is: {grade}")

