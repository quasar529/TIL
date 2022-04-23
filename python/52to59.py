# 52
import random
print(random.randint(1, 100))

# 53
fruits = random.choice(["apple", "banana", "kiwi", "pear", "peach"])
print(fruits)

# 54
hort = random.choice(['h', 't'])
user = input("h or t: ")
if hort == user:
    print("You win!")
else:
    print("Bad luck")

# 55
num = random.randint(1, 5)
user = int(input("Enter a num: "))
if user == num:
    print("Well done.")
elif user < num:
    user = int(input("Too low, try again: "))
    if user != num:
        print("You lose")
    elif user == num:
        print("Correct")
elif user > num:
    user = int(input("Too high, try again: "))
    if user != num:
        print("You lose")
    elif user == num:
        print("Correct")

# 56
num = random.randint(1, 10)
user = int(input("Enter a num: "))
while num != user:
    user = int(input("Try agian: "))

# 57
num = random.randint(1, 10)
user = int(input("Enter a num: "))
while num != user:
    if num < user:
        user = int(input("Too high, Try agian: "))
    elif num > user:
        user = int(input("Too low, Try agian: "))

# 58
cnt = 0
for i in range(5):
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    ans = num1+num2
    user = int(input("{} + {} = ? ".format(num1, num2)))
    if user == ans:
        cnt += 1
print("count is {}".format(cnt))

# 59
colors = ["red", "blue", "green"]
color = random.choice(colors)
user = input(colors)
if color == user:
    print("well done")
