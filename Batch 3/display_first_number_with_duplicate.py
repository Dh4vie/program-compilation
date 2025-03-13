#get 10 numbers
numbers = []
num_with_dupe = set()

print("Enter 10 numbers")
for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)

#find the first number of numbers with duplicates
for num in numbers:
    if num not in num_with_dupe:
        num_with_dupe.add(num)

#print the first number of numbers with duplicates
    print(num)