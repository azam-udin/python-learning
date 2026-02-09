# Creating tuples
coordinates = (10, 20)
colors = ("red", "green", "blue")

# Printing tuples
print("Coordinates:", coordinates)
print("Colors:", colors)

# Accessing elements
print("\nX coordinate:", coordinates[0])
print("Y coordinate:", coordinates[1])

# Tuples are immutable - this would cause an error:
# coordinates[0] = 15  # TypeError!

# Unpacking tuples
x, y = coordinates
print(f"\nUnpacked: x = {x}, y = {y}")
