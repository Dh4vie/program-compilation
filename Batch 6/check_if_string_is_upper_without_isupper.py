#create a string
statement = str(input("Make any statement: "))

#check if string is upper without using .isupper
def isupper_replacement(string):
    return string == string.upper()

#print if true or false
print(isupper_replacement(statement))