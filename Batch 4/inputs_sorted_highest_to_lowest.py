#get user inputs and loop until invalid
numbers = []

while True:
    try:
        num = int(input("Enter a Number: "))
        numbers.append(num)
    except ValueError:
        break
#sort inputs highest to lowest
if numbers:
    numbers.sort(reverse=True)
#print the sorted inputs
    print(numbers)
else:
    print("no numbers were entered.")