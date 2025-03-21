#Ask user for input
name = input("Enter name with spaces at the beginning: ")

#Remove spaces
fixed_name = name.lstrip()

#Print result
print(fixed_name)