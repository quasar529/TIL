# 27

import math
alotofnum = float(input("Enter a num: "))
print(alotofnum*2)

# 28
print(round(alotofnum, 2))

# 30

print(round(math.pi, 5))

# 31
r = float(input("Enter a r"))
area = r * r * math.pi
print(area)

# 32
r = float(input("Enter a r "))
h = float(input("Enter a h :"))
volume = r*r*math.pi*h
print(round(volume, 3))

# 33
num1 = int(input())
num2 = int(input())
quo = num1/num2
mod = num1 % num2
print("{} is divided by {} is {} with {} remaining".format(num1, num2, quo, mod))

# 34
print("1) Square\n2) Triangle\n\n")
num = int(input("Enter a number: "))
if num is 1:
    lenofside = int(input("Enter a length: "))
    print(lenofside**2)
elif num is 2:
    lenofside = int(input("Enter a length: "))
    lenofheight = int(input("Enter a height"))
    print(lenofheight*lenofside/2)
else:
    print("Your input is wrong")
