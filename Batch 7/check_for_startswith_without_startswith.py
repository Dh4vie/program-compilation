#create string
statement = str(input("Make any statement: ")).rstrip()
prefix = "hello"

#check if word ends with parameter without endswith
def startswith_replacement(string, prefix):
    return string[:len(prefix)] == prefix if len(prefix) <= len(string) else False

#print if true or false
print(startswith_replacement(statement, prefix))