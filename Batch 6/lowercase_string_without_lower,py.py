#create a string
statement = str(input("make any statement to convert into lowercase: "))

#convert the string to lowercase without using lower
statement_fix = statement.casefold()
print(statement_fix)