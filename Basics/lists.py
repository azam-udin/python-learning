# Creating lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

# Printing lists
print("Fruits:", fruits)
print("Numbers:", numbers)
print("Mixed:", mixed)

# Accessing elements
print("\nFirst fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Modifying lists
fruits.append("orange")  # Add to end
print("\nAfter adding orange:", fruits)

fruits.insert(1, "grape")  # Insert at position
print("After inserting grape:", fruits)

fruits.remove("banana")  # Remove item
print("After removing banana:", fruits)

# List slicing
print("\nFirst two fruits:", fruits[0:2])
print("All fruits:", fruits[:])