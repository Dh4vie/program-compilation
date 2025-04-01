#create a string
statement = str(input("Input any statement with spaces on end: "))

#remove spaces
def remove_end_space(string):
    index = len(string) - 1
    while index >= 0 and string[index] == ' ':
        index -= 1
    return string[:index+1]

#print output
print(remove_end_space(statement))