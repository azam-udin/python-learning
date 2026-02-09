# Ask the user to enter their name
name = input("Enter your name: ")

# Use a loop to go through each letter in reverse and print it with its position
for position, letter in enumerate(reversed(name), start=1):
    print(f"{letter} {len(name) - position + 1}")