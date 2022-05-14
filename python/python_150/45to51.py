# 45
total = 0
while total <= 50:
    num = int(input("Enter a num: "))
    total += num
    print("The total is...", total)

# 46
num = int(input("Enter a num: "))
while num <= 5:
    num = int(input("Enter again: "))
print("The last num you entered was a", num)

# 47
num = int(input("Enter:"))
num2 = int(input("Enter again: "))
sum = num+num2
choice = input("y?: ")
while choice == 'y':
    num3 = int(input("Enter another: "))
    sum += num3
    choice = input("y?: ")
print(sum)

# 48
name = input("Enter a name: ")
print(name, "has now been invited.")
count = 1
ask = input("invite more? y or n: ")
while ask == 'y':
    name = input("Enter a name: ")
    print(name, "has now been invited.")
    count += 1
    ask = input("invite more? y or n: ")


print(count)

# 49
compnum = 50
num = int(input("Enter: "))
count = 1
while compnum != num:
    count += 1
    if compnum < num:
        num = int(input("Your num is higher than answer. Try again: "))
    else:
        num = int(input("Your num is lower than answer. Try again: "))
print("Well done, you took {} attemps".format(count))

# 50
num = int(input("Enter a num between 10 and 20: "))
while num <= 10 or num >= 20:
    if num <= 10:
        num = int(input("Too low, try again: "))
    elif num >= 20:
        num = int(input("Too high, try again: "))

print("Thank you")

# 51
