#crete a string
statement = str(input("Input any statement: "))

#capitalize the string without .capitalize
statement_capitalized = statement[0].upper() + statement[1:].lower()

#print output
print(statement_capitalized)