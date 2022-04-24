# 80
firstname = input("Enter first name: ")
print(len(firstname))
lastname = input("Enter lastname: ")
print(len(lastname))
name = firstname+' '+lastname
print(name, '\n', len(name))

# 81
user = input("favorite subject: ")
for i in user:
    print(i, end='-')

# 82
poem = """
i'm awfully difficult
but i do know when i love someone
and i've loved you
ever since i can remember
"""
print(poem)
startindex = int(input("start: "))
endindex = int(input("end: "))
print(poem[startindex:endindex])

# 83
user = input("Upper message: ")
tryagain = True
while tryagain:
    if user.isupper():
        tryagain = False
        print("good", user)
    else:
        user = input("Try again")

# 84
user = input("Enter: ")
for i in range(2):
    print(user[i].upper())

# 85
name = input("name: ")
cnt = 0
for i in name:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        cnt += 1
print(cnt)

# 86
password = input("password: ")
confirm = input("Enter again: ")
if password == confirm:
    print("Thank you")
elif password.lower() == confirm.lower():
    print("must be in the same case")
else:
    print("Incorrect")

# 87
user = input("enter: ")
for i in range(len(user)-1, -1, -1):
    print(user[i])
