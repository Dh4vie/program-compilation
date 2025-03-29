#create a string
statement = str(input("make a statement that starts with 'hello': "))

#remove the prefix without using removeprefix
staement_fix = statement.replace("hello", "").lstrip()
print(staement_fix)