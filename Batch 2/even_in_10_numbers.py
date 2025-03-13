even = 0
numbers = [float(input(f'input number {num + 1}: '))for num in range(10)]

for num in numbers:
    if num % 2 == 0:
        even += 1

print(even)