#ask user to input until invalid
numbers = []

while True:
    try: 
        num = int(input("Enter a Number: "))
        numbers.append(num)
    except ValueError:
        break

#find most duplicated nunber
if numbers:
    most_dupe = max(numbers, key = numbers.count)
    
#display most duplicated number
    print(most_dupe)
else:
    print('no numbers were entered')
