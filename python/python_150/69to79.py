# 69
from turtle import color

from soupsieve import select


country = ("kor", "usa", "chi", "fra", "ger")
user = input(country)
print(country.index(user))

# 70
num = int(input("Enter a num "))
country = ("kor", "usa", "chi", "fra", "ger")
print(country[num])

# 71
sports = ["football", "tennis"]
user = input("your favorite sports? ")
sports.append(user)
sports.sort()
print(sports)

# 72
subjects = ["math", "eng", "kor", "sci"]
user = input("subject you hate: ")
subjects.remove(user)
print(subjects)

# 73
dict = {}
for i in range(1, 5):
    user = input("Your favorite food: ")
    dict[i] = user

print(dict)
user = int(input("del food: "))
del dict[user]
print(sorted(dict.values()))

# 74
colors = ["red", "blue", "green", "yellow", "grey",
          "black", "purple", "orange", "brown", "emerald"]
startnum = int(input("0to4: "))
endnum = int(input("5to9: "))
print(colors[startnum:endnum+1])

# 75
nums = [101, 203, 405, 608]
for i in nums:
    print(i)
user = int(input("Enter a num:  "))
if user in nums:
    print("index: ", nums.index(user))
else:
    print("No")

# 76
invite = []
for i in range(3):
    user = input("invite name: ")
    invite.append(user)
user = input("y or n: ")
while user == 'y':
    temp = input("name: ")
    invite.append(temp)
    user = input("y or n: ")
print("how many: ", len(invite))

# 77
invite = []
for i in range(3):
    user = input("invite name: ")
    invite.append(user)
print(invite)
user = input("y or n: ")
while user == 'y':
    temp = input("name: ")
    invite.append(temp)
    user = input("y or n: ")

print(invite)
selection = input("choose a name: ")
yorn = input("index: {}, y or n?".format(invite.index(selection)))
if yorn == 'n':
    invite.remove(selection)
print(invite)

# 78
tvs = ["무한도전", "유퀴즈", "런닝맨", "브루클린나인나인"]
for i in tvs:
    print(i)
name = input("Tv name ? ")
userindex = int(input("enter a index: "))
tvs.insert(userindex, name)
print(tvs)

# 79
nums = []
for i in range(3):
    user = int(input("enter a num: "))
    nums.append(user)
    print(nums)
yorn = input("y or n: ")
if yorn == "n":
    del nums[2]
print(nums)
