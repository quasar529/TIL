# 88
import math
import random
from array import *
nums = array('i', [])
for i in range(5):
    num = int(input("Enter a num: "))
    nums.append(num)
nums = sorted(nums)
nums.reverse()
print(nums)

# 89

nums = array('i', [])
for i in range(5):
    temp = random.randint(1, 100)
    nums.append(temp)
for i in sorted(nums):
    print(i)

# 90
nums = array('i', [])
for i in range(5):
    user = int(input("Enter: "))
    if user >= 10 and user <= 20:
        nums.append(user)
    else:
        print("Outside the range")

if len(nums) == 5:
    print("Thank you")

# 91
nums = array('i', [12, 12, 14, 51, 23])
print(nums)
user = int(input("Choose a number: "))

print(nums.count(user))

# 92
nums1 = array('i', [])
nums2 = array('i', [])
for i in range(5):
    nums2.append(random.randint(1, 100))

for i in range(3):
    user = int(input("Enter a num: "))
    nums1.append(user)

nums1.extend(nums2)
for i in nums1:
    print(i)

# 93
nums = array('i', [])
for i in range(5):
    user = int(input("enter: "))
    nums.append(user)
print(nums)
user = int(input("Choose a num: "))
nums.remove(user)

newNums = array('i', [])
newNums.append(user)

# 94
nums = array('i', [23, 43, 34, 32, 14])
print(nums)
user = int(input("choose: "))

while 1:
    if user in nums:
        print(nums.index(user))
        break
    else:
        user = int(input("choose again: "))

# 95
nums = array('f', [31.41, 15.92, 23.43, 99.99, 77.55])
while 1:
    user = int(input("Enter a num between 2 and 5: "))
    if user < 2 or user > 5:
        user = int(input("Try AGAIN"))
    else:
        for i in nums:
            print(round(i/user, 2))
        break
