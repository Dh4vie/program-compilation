#create a string
statement = str(input("Input any statement/Word: "))

#set a parameter to center the string
def center_replacement(string):
    if len(string) >= 15:
        return string
    total_spaces = 15 - len(string)
    left_spaces = total_spaces // 2
    right_spaces = total_spaces - left_spaces
    return " " * left_spaces + string + right_spaces * " "

#print output
print("'" + center_replacement(statement) + "'")