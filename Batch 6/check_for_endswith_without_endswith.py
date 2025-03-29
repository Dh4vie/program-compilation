#create a string 
statement = str(input("Make any statement: ")).rstrip()
suffix = "anything"

#check if word ends with parameter without endswith
def endswith_replacement(string, suffix):
    return string[-len(suffix):] == suffix if len(suffix) <= len(string) else False

#print if true or false
print(endswith_replacement(statement, suffix))