total = 0
count = 0

while count < 5:
    num = float(input(f"Enter number {count + 1}: "))
    total += num
    count += 1

print(f"The total is: {total}")
