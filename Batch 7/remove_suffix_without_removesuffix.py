#create string
statement = str(input("Make a statement that ends with 'bye': "))

#remove suffix without .removesuffix
if statement.endswith("bye"):
    statement_fix = statement[:-3].rstrip()
else:
    statement_fix = statement

#print outputs
print(statement_fix)