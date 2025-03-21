#Ask user for number input
num = int(input('Enter a number from 0-1000: '))

#Format number into 6-digits
num_format = f'{num:06d}'

#Print result
print(num_format)