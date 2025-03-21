#Ask user input
name = input('Enter fullname(preferably in incorrect casing): ')

#format to pascal case
pascal_case_name = name.title().replace(" ", "")

#print result
print(pascal_case_name)