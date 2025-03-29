#create a string
statement = str(input("Make any statement: "))

#capitalize every word without using .title
title_case_statement = " ".join(word.capitalize() for word in statement.split())

#print output
print(title_case_statement)