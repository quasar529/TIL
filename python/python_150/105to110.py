# 105
file = open("Numbers.txt", 'w')
file.write("1,2,3,4,5\n")
file.close()

# 106
file = open("Names.txt", 'w')
file.write("Wade\n")
file.write("Steven\n")
file.write("Mo\n")
file.write("Arnold\n")
file.write("Milner\n")
file.close()

# 107
file = open("Names.txt", 'r')
print(file.read())
file.close()

# 108
file = open("Names.txt", 'a')
name = input("Enter a name: ")
file.write(name+'\n')
file.close()

file = open("Names.txt", 'r')
print(file.read())
file.close()

# 109
print("1) create a new file\n2) Display the file\n3)Add a new item to the file")
user = int(input("Make a selection 1,2, or 3: "))
if user != 1 and user != 2 and user != 3:
    print("ERROR")
elif user == 1:
    subject = input("Enter a subject: ")
    file = open("Subject.txt", 'w')
    file.write(subject+'\n')
    file.close()
elif user == 2:
    file = open("Subject.txt", 'r')
    print(file.read())
    file.close()
elif user == 3:
    subject = input("new subject: ")
    file = open("Subject.txt", 'a')
    file.write(subject+'\n')
    file.close()
    file = open("Subject.txt", 'r')
    print(file.read())
    file.close()

# 110
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
