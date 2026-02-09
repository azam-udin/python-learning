# Bill Splitter - Mini Project 1
print("=" * 50)
print("         BILL SPLITTER CALCULATOR")
print("=" * 50)

# Get total bill amount from user
total_bill = float(input("\nEnter the total bill amount: $"))

# Validate bill amount
if total_bill < 0:
    print("Error: Bill amount cannot be negative!")
    exit()

# Get number of people
num_people = int(input("Enter the number of people: "))

# Validate number of people
if num_people <= 0:
    print("Error: Number of people must be greater than 0!")
    exit()

# Calculate amount per person
amount_per_person = total_bill / num_people

# Display results
print("=" * 50)
print("                   RESULTS")
print("=" * 50)
print(f"Total Bill Amount:    ${total_bill:}")
print(f"Number of People:     {num_people}")
print("-" * 50)
print(f"Amount per Person:    ${amount_per_person:}")
print("=" * 50)
