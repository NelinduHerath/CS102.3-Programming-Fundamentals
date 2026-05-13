low = 0
medium = 0
high = 0

for i in range(10):
    amount = float(input(f"Enter bill amount for transaction {i+1}: "))

    if amount < 1000:
        low += 1
    elif amount > 5000:
        high += 1
    else:
        medium += 1

print("\nSales Summary:")
print("Low-value sales:", low)
print("Medium-value sales:", medium)
print("High-value sales:", high)
