#create a string
statement = str(input("Make any statement: "))

#set a specific number of spaces to fit a certain parameter
def lstring_replacement(string):
    return string if len(string) >= 10 else string + " " * (10 - len(string))

#print output
print("'" + lstring_replacement(statement) + "'")