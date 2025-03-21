#Ask user input
name = input('Enter Full name: ')

#format to snake case
snake_case_name = name.lower().replace(" ", "_")

#print result
print(snake_case_name)