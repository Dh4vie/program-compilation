#create string
statement = str(input("make any statement to convert into uppercase: "))

#covert to uppercase without upper
def upper_replacement(string):
    result = ''
    for char in string:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    return result
    
#print output
print(upper_replacement(statement))