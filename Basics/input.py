#getting input from user
name = input("Enter your name: ")
age = input("Enter your age: ")

#convert string input to integer
age = int(age)

#diplay output
print(f"Hello, {name}! You are {age} years old.")

#multiple outputs
print("Line 1", "Line 2", "Line 3", sep=" | ") #custom separator
print("Line 1", "Line 2", "Line 3", sep="  ")
print("First", end="\n") #new line at the end
print("Second", end=" ")
print("Third")