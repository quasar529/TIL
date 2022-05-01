file = open("Names.txt", 'r')
print(file.read())
file.close()
file = open("Names.txt", 'r')
user = input("Enter a name of them: ")
user = user+'\n'
for row in file:
    if row != user:
        file = open("Names2.txt", 'a')
        file.write(row)
        file.close()
file = open("Names2.txt", 'r')
print(file.read())
file.close()
