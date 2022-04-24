nums=[]
for i in range(3):
    user= int(input("enter a num: "))
    nums.append(user)
    print(nums)
yorn= input("y or n: ")
if yorn=="n":
    del nums[2]
print(nums)