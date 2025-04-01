#create string
statement = str(input("Enter a statement: "))

#set a specific number of spaces to fit a certain parameter
def rjust_replacement(string):
    return " " * (15 - len(string)) + string if len(string) < 15 else string

#print output
print(rjust_replacement(statement))