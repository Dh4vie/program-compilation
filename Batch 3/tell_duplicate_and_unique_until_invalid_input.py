#get inputs
numbers = set()

while True:
    try:
        num = int(input("enter a number: "))
#print if number is duplicate or unique
        if num in numbers:
            print("Duplicate")
        else:
            print("Unique")
            numbers.add(num)
#exit program if invalid input
    except ValueError:
        print("Exit..")
        break