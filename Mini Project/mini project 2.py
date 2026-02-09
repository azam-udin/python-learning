# BMI Calculator Project
# Get user information
name = input("Name: ")
weight = float(input("Weight (kg): "))
height = float(input("Height (m): "))

# Calculate BMI
bmi = weight / (height ** 2)

# Determine weight category based on BMI
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal Weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

# Print results
print(f"--- BMI Results for {name} ---")
print(f"Weight: {weight} kg")
print(f"Height: {height} m")
print(f"BMI: {bmi:.2f}")
print(f"Weight Category: {category}")