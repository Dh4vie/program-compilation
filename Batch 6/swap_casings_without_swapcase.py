#create a string
statement = str(input("Make any statement: "))

#reverse casing without swapcase
def swapcase_replacement(string):
    output = ""
    for letter in string:
        if letter.islower():
            output += letter.upper()
        elif letter.isupper():
            output += letter.lower()
        else:
            output += letter
    return output

#print output
print(swapcase_replacement(statement))