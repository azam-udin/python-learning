# Create a set
fruits = {"apple", "banana", "cherry", "apple"}  # duplicate 'apple' ignored
print(fruits)
# Output: {'banana', 'apple', 'cherry'}

# Add an item
fruits.add("orange")
print(fruits)

# Remove an item
fruits.remove("banana")
print(fruits)

# Check membership
print("apple" in fruits)   