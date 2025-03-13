#get user inputs and loop until invaild
lowest_num = None

while True:
    try:
        num = int(input("Enter a number: "))
        if lowest_num is None or num < lowest_num:
            lowest_num = num
    except ValueError:
        break

#print the lowest value
if lowest_num is not None:
    print("lowest input:", lowest_num)
else:
    print("no numbers were entered")