#create string
statement = str(input("Enter a statement: "))

#fill desired length with zeros without zfill
def zfill_replacement(string):
    return "0" * (10 - len(string)) + string if len(string) < 10 else string

#print output
print(zfill_replacement(statement))