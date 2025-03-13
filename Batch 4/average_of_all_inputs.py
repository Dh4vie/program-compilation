#get user inputs til invalid
numbers = []

while True:
    try:
        num = float(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        break

#calculate the average of all inputs
if numbers:
    average = sum(numbers) / len(numbers)
#display the average
    print(average)
else:
    print("no numbers were entered")