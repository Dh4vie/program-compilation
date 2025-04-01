#create a string
statement = str(input("make a statement that starts with 'hello': "))

#remove the prefix without using removeprefix
if statement.startswith("hello"):
    statement_fix = statement[5:].lstrip()
else: 
    statement_fix = statement
print(statement_fix)