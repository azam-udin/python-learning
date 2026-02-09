# Reading entire file
with open("example.txt", "r") as file:
    content = file.read()
    print("File content:")
    print(content)

# Reading line by line
with open("example.txt", "r") as file:
    print("\nReading line by line:")
    for line in file:
        print(line.strip())  # strip() removes newline characters

# Reading all lines into a list
with open("example.txt", "r") as file:
    lines = file.readlines()
    print("\nAll lines:")
    for i, line in enumerate(lines, 1):
        print(f"Line {i}: {line.strip()}")