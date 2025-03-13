#get 10 user inputs
def get_no_duplicate_numbers():
    numbers = []

    print("Enter 10 numbers")
    for i in range(10):
        num = int(input("Enter number: "))
        numbers.append(num)

#find numbers with no duplicates
        no_duplicate_numbers = []
        for num in numbers:
            if numbers.count(num) == 1:
                no_duplicate_numbers.append(num)

#print the numbers without duplicates
    print(no_duplicate_numbers)

get_no_duplicate_numbers()