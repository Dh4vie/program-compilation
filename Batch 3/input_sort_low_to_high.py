#get user inputs
numbers = []

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        break

#sort inputs hughest to lowest
if numbers:
    numbers.sort()

#print inputs
    print(numbers)
else:
    print("no numbers were entered.")