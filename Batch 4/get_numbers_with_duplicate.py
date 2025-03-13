#get user inputs
numbers = []

print("Enter 10 numbers")
for i in range(10):
    num = int(input("Enter a number:"))
    numbers.append(num)

#find numbers with duplicates
num_with_duplicate = []
for num in numbers:
    if numbers.count(num) != 1:
        num_with_duplicate.append(num)

#print numebrs with duplicates
print(num_with_duplicate)