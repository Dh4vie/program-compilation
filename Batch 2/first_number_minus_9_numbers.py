numbers = [float(input(f'input number {num + 1}: '))for num in range(10)]

result = numbers[0] - sum(numbers[1:])
print(result)