#get user inputs until invalid
highest_num = None 

while True:
    try:
        num = int(input("Enter a number: "))
#find the highest number 
        if highest_num is None or num > highest_num:
            highest_num = num
    except ValueError:
        break

#print the highest number
if highest_num is not None:
    print(highest_num)
else:
    print("no numbers were entered")