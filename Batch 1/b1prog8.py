odd = 0
numbers = [float(input(f"input number {num + 1}: "))for num in range(10)]

for num in numbers:
    if num % 2 != 0:
        odd += 1

print(odd)