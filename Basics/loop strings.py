#Iterating through a string
word = "Python"

print("Letters in 'Python':")
for letter in word:
    print(letter)

#Iterating through a list
fruits = ["apple", "banana", "cherry"]
print("\nFruits:")
for fruit in fruits:
    print(f"I like {fruit}")

#Nested loops: iterating through letters of each fruit
fruits = ["apple", "banana", "cherry"]
print("\nFruits:")
for fruit in fruits:
    for letters in fruit:
        print(letters)
        print("\n")