# 35
name = input("Enter your name: ")
for i in range(1, 10):
    print(name)

# 36
name = input("Enter your name: ")
num = int(input("Enter a num: "))
for i in range(0, num):
    print(name)
# 37
name = input("Enter your name: ")
for i in name:
    print(i)
# 38
name = input("Enter your name: ")
num = int(input("Enter a num: "))

for x in range(0, num):
    for i in name:
        print(i)
# 39
num = int(input("Enter a num between 1 and 12: "))
for i in range(1, 13):
    print(num*i)

# 40
num = int(input("Enter a num under 50: "))
for i in range(50, num-1, -1):
    print(i)

# 41
name = input("Enter a name: ")
num = int(input("Enter a num: "))
if num >= 10:
    for i in range(0, 3):
        print("Too high")
else:
    for i in range(0, num):
        print(name)

# 42
total = 0
for i in range(5):
    num = int(input("ENter a num: "))

    choice = input("Do you want to plus? YES or NO")
    if choice == "YES":
        total += num
    elif choice == "NO":
        continue
print(total)

# 43
upordown = input("up or down")
if upordown == "up":
    num = int(input("Enter a num: "))
    for i in range(1, num+1):
        print(i)
elif upordown == "down":
    num = int(input("Enter a num below 20: "))
    for i in range(20, num-1, -1):
        print(i)
else:
    print("I don't understand")

# 44
num = int(input("Enter how many people you want to invite: "))
if num < 10:
    for i in range(num):
        name = input("Enter a name: ")
        print(name, "has been invited.\n")
else:
    print("Too many people")
