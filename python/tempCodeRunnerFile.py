
import random

def twoNums():
    sum = random.randint(5,20) + random.randint(5,20)
    user = int(input("sum of two nums?"))
    data_tuple = (user,sum)
    return data_tuple

def subtraction():
    ans=random.randint(25,50) - random.randint(1,25)
    user = int(input("your answer? "))
    data_tuple = (user,ans)
    return data_tuple

def checkFunc(user,ans):
    if user==ans:
        print("Correct")
    else:
        print("Incorrect",ans)
    
def user_choice():
    user = int(input("1) Addtion\n2) Subtraction\nEnter 1 or 2: "))
    if user == 1:
        userans,realans=twoNums()
        checkFunc(userans,realans)
    elif user==2:
        userans,realans=subtraction()
        checkFunc(userans,realans)
    else:
        print("Your input is wrong")
def main():
    user_choice()
main()