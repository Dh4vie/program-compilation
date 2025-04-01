#create string
statement = str(input("Make a statement: "))

#check if string is lowercase without islower
def islower_replacement(string):
    for char in string:
        if 'A' <= char <= 'Z':
            return False
    return True

#print output
print(islower_replacement(statement))