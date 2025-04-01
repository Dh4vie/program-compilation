#create string
statement = str(input("Enter a statement: "))
counted_character = "a"

#count a certain parameter
def count_replacement(string, count_char):
    count = 0
    for i in range(len(string) - len(count_char) + 1):  
        if string[i:i+len(count_char)] == count_char:  
            count += 1
    return count

#print output
print(count_replacement(statement, counted_character)) 