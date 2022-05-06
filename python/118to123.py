# 118
import csv
from distutils.dep_util import newer
from operator import mod
import random


def requireNum():
    num = int(input("Enter a num: "))
    return num


def countToNum(num):
    for i in range(1, num+1):
        print(i)


def main():
    num = requireNum()
    countToNum(num)


main()

# 119


def twoNums():
    lownum = int(input("low num: "))
    highnum = int(input("high num: "))
    comp_num = random.randint(lownum, highnum)
    return comp_num


def usernum():
    num = int(input("I am thinking of a number..."))
    return num


def checkfunc(comp_num, num):
    while 1:
        if num == comp_num:
            print("Correct, you win!")
            break
        else:
            if num > comp_num:
                num = int(input("Too high, try again."))
            else:
                num = int(input("Too low, try again."))


def main():
    checkfunc(twoNums(), usernum())


main()

# 120


def twoNums():
    sum = random.randint(5, 20) + random.randint(5, 20)
    user = int(input("sum of two nums?"))
    data_tuple = (user, sum)
    return data_tuple


def subtraction():
    ans = random.randint(25, 50) - random.randint(1, 25)
    user = int(input("your answer? "))
    data_tuple = (user, ans)
    return data_tuple


def checkFunc(user, ans):
    if user == ans:
        print("Correct")
    else:
        print("Incorrect", ans)


def user_choice():
    user = int(input("1) Addtion\n2) Subtraction\nEnter 1 or 2: "))
    if user == 1:
        userans, realans = twoNums()
        checkFunc(userans, realans)
    elif user == 2:
        userans, realans = subtraction()
        checkFunc(userans, realans)
    else:
        print("Your input is wrong")


def main():
    user_choice()


main()


# 121
names = []


def add_name():
    name = input("NAME:? ")
    names.append(name)
    return names


def show_name():
    x = 0
    for name in names:
        print(x, ' ', name)
        x += 1
    print('\n')


def modify_name():
    show_name()
    user = int(input("Which name you want to modify? choose index: "))
    newName = input("New Name: ")
    names[user] = newName
    return names


def del_name():
    show_name()
    user = int(input("Which name you want to delete? choose index: "))
    del names[user]
    return names


def main():
    while 1:
        user = int(input("Menu\n1)add\n2)modify\n3)delete\n4)show\n5)END\n"))
        if user == 1:
            add_name()
        elif user == 2:
            modify_name()
        elif user == 3:
            del_name()
        elif user == 4:
            show_name()
        elif user == 5:
            break


main()

# 122


def addToFile():
    file = open("Salaries.csv", 'a')
    name = input("Enter a name: ")
    salary = input("Salary: ")
    newRecord = name+','+salary+'\n'

    file.write(str(newRecord))
    file.close()


def viewAllRecords():
    file = open("Salaries.csv", 'r')
    for row in file:
        print(row)


def main():
    while 1:
        user = int(input(
            "1) Add to file\n2)View all records\n3)Quit program\n\nEnter the number of your selection: "))
        if user == 3:
            break
        elif user == 1:
            addToFile()
        elif user == 2:
            viewAllRecords()
        else:
            print("Wrong input, try again")


main()

# 123


def addToFile():
    file = open("Salaries.csv", 'a')
    name = input("Enter a name: ")
    salary = int(input("Salary: "))
    newRecord = name+','+str(salary)+'\n'

    file.write(str(newRecord))
    file.close()


def viewAllRecords():
    file = open("Salaries.csv", 'r')
    for row in file:
        print(row)
    file.close()


def deleteARecord():
    file = open("Salaries.csv", 'r')
    tmp = []
    for row in file:
        tmp.append(row)
    file.close()

    x = 0
    for row in tmp:
        print(x, ' ', row)
        x += 1
    delrcd = int(input("Choose a row to delete: "))
    del tmp[delrcd]

    file = open("Salaries.csv", 'w')
    for row in tmp:
        file.write(row)

    file.close()


def main():
    while 1:
        user = (input(
            "1)Add to file\n2)View all records\n3)Delete a Record\n4)Quit program\n\nEnter the number of your selection: "))
        if user == '4':
            break
        elif user == '1':
            addToFile()
        elif user == '2':
            viewAllRecords()
        elif user == '3':
            deleteARecord()
        else:
            print("Wrong input, try again")


main()
