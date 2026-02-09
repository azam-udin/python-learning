# Creating dictionaries
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

print("Student:", student)

# Accessing values
print("\nName:", student["name"])
print("Age:", student.get("age"))

# Adding/updating values
student["email"] = "alice@example.com"
student["age"] = 21
print("\nUpdated student:", student)

# Removing items
del student["grade"]
print("After removing grade:", student)

# Dictionary methods
print("\nKeys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())