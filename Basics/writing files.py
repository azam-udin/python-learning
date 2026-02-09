# Writing to a file (overwrites existing content)
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a new file.\n")
    file.write("Python is great!")

print("File written successfully!")

# Appending to a file
with open("output.txt", "a") as file:
    file.write("\nThis line was appended.")
    file.write("\nMore content added.")

print("Content appended successfully!")

# Writing multiple lines
lines_to_write = [
    "Line 1",
    "Line 2",
    "Line 3"
]

with open("output.txt", "w") as file:
    file.writelines("\n".join(lines_to_write))

print("Multiple lines written!")