# Travel Eligibility Checker
print("=" * 50)
print("          TRAVEL ELIGIBILITY CHECKER")
print("=" * 50)

age = int(input("\nEnter your age: "))
has_parental_guide = True
have_passport = False

print("\n" + "-" * 50)
print("YOUR INFORMATION:")
print("-" * 50)
print(f"Age: {age} years old")
print(f"Has Parental Guide: {has_parental_guide}")
print(f"Has Passport: {have_passport}")

print("\n" + "-" * 50)
print("TRAVEL ELIGIBILITY RESULT:")
print("-" * 50)

if age < 16:
    if has_parental_guide:
        print("✓ You CAN travel with a parental guide.")
    else:
        print("✗ You CANNOT travel. You need a parental guide.")
else:
    if have_passport:
        print("✓ You CAN travel internationally.")
    else:
        print("✗ You CANNOT travel internationally. You need a passport.")

print("\n" + "=" * 50)
    