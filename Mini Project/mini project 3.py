# Ask the user to enter their name
name = input("Enter your name: ")

# Use a loop to go through each letter and print it with its position
for position, letter in enumerate(name, start=1):
    print(f"{letter} {position}")