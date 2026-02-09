# BMI Calculator Project

# Get user information
name = input("What is your name? ")
weight = float(input("What is your weight (kg)? "))
height = float(input("What is your height (m)? "))

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
print(f"\n--- BMI Results for {name} ---")
print(f"Weight: {weight} kg")
print(f"Height: {height} m")
print(f"BMI: {bmi:.2f}")
print(f"Weight Category: {category}")
