#create a string
statement = str(input("Enter a statement: "))
char_find = 'a'

#create a certain paramter and make it function similar to rindex
def rindex_replacement(string, search_char):
    for i in range(len(string) - len(search_char), -1, -1):
        if string[i:i+len(search_char)] == search_char:  
            return i  
    raise ValueError(f"'{search_char}' not found in the string")

#print output
try:
    print(rindex_replacement(statement, char_find))
except ValueError as e:
    print(e)