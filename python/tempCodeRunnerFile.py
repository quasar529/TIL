from array import *
import math
nums = array('f',[31.41,15.92,23.43, 99.99,77.55])
while 1:
    user = int(input("Enter a num between 2 and 5: "))
    if user <2 or user > 5:
        user = int(input("Try AGAIN"))
    else:
        for i in nums:
            print(round(i/user,2))
        break