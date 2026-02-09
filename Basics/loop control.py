# Using break
print("Finding first even number:")
for num in range(1, 10):
    if num % 2 == 0:
        print(f"Found: {num}")
        break  # Exit loop immediately

# Using continue
print("\nPrinting odd numbers:")
for num in range(1, 10):
    if num % 2 == 0:
        continue  # Skip to next iteration
    print(num)
