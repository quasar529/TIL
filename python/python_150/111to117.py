# csv
import random
import csv

file = open("Stars.csv", 'w')
newRecord = "Brain,73,Taurus\n"
file.write(str(newRecord))
file.close()

file = open("Stars.csv", 'a')
name = input("Enter name: ")
age = input("Enter age: ")
star = input("star: ")
newRecord = name+','+age+','+star+'\n'
file.write(str(newRecord))
file.close()

file = open("Stars.csv", 'r')
for row in file:
    print(row)

file = open("Stars.csv", 'r')
reader = csv.reader(file)
rows = list(reader)
print(row[1])

file = open("Stars.csv", 'r')
search = input("Enter what you want to search: ")
for row in file:
    if search in str(row):
        print(row)

file = list(csv.reader(open("Stars.csv")))
tmp = []
for row in file:
    tmp.append(row)

file = open("NewStars.csv", 'w')
x = 0
for row in tmp:
    newRec = tmp[x][0] + ','+tmp[x][1]+','+tmp[x][2]+'\n'
    file.write(newRec)
    x = x+1
file.close()


# 111
file = open("Books.csv", 'w')
record0 = "To Kill A Mockingbird,Harper Lee,1960\n"
file.write(str(record0))
record1 = "A Brief History of Time,Stephen Hawking,1988\n"
file.write(str(record1))
record2 = "The Great Gatsby,F. Scott Fitzgerald,1922\n"
file.write(str(record2))
record3 = "The Man Who Mistook His Wife for a Hat,Oliver Sacks,1985\n"
file.write(str(record3))
record4 = "Pride and Prejudice,Jane Austin,1813\n"
file.write(str(record4))
file.close()
# 112
file = open("Books.csv", 'a')
title = input("Book title: ")
author = input("author: ")
date = input("publish date: ")
newRecord = title+','+author+','+date+'\n'
file.write(str(newRecord))
file.close()

file = open("Books.csv", 'r')
for row in file:
    print(row)

# 113
file = open("Books.csv", 'a')
howmany = int(input("How many new records you want? "))
for i in range(howmany):
    title = input("Book title: ")
    author = input("author: ")
    date = input("publish date: ")
    newRecord = title+','+author+','+date+'\n'
    file.write(str(newRecord))

file.close()

file = open("Books.csv", 'r')
search = input("What you want to search? ")
for row in file:
    if search in str(row):
        print(row)
print("There is no author you want to search")

# 114

startYear = int(input("Start year: "))
endYear = int(input("End year: "))
tmp = []
file = list(csv.reader(open("Books.csv")))
for row in file:
    tmp.append(row)

for row in tmp:
    if int(row[2]) > startYear and int(row[2]) < endYear:
        print(row[0])

# 115
x = 0
file = open("Books.csv", 'r')
for row in file:
    print(x, ' ', row)
    x += 1

# 116
file = list(csv.reader(open("Books.csv")))
tmp = []
x = 0
for row in file:
    tmp.append(row)
    print(x, ' ', row)
    x += 1

user = int(input("Which row you want to delete? "))
del tmp[user]

x = 0
for row in tmp:
    print(x, ' ', row)
    x += 1

user = int(input("Which row you want to modify? "))

part = int(input("Which part you want to change: "))
newData = input("new Data: ")

tmp[user][part] = newData

for row in tmp:
    print(row)

file = open("Books.csv", 'w')

for row in tmp:
    newRecord = row[0]+','+row[1]+','+row[2]+'\n'
    file.write(str(newRecord))
file.close()

file = open("Books.csv", 'r')
for row in file:
    print(row)

# 117
name = input("Enter your name: ")
score = 0
rdn1 = random.randint(1, 100)
rdn2 = random.randint(1, 100)
question1 = str(rdn1)+" + " + str(rdn2) + " = "
userans = int(input(question1))
realans = rdn1+rdn2
if realans == userans:
    score += 1

rdn3 = random.randint(100, 1000)
rdn4 = random.randint(100, 1000)
question2 = str(rdn3)+" + " + str(rdn4) + " = "
userans2 = int(input(question2))
realans2 = rdn3+rdn4
if realans2 == userans2:
    score += 1

file = open("QuizScore.scv", 'w')
newRecord = name+','+(question1)+','+str(userans)+',' + \
    (question2)+','+str(userans2)+','+str(score)
file.write(str(newRecord))
file.close()

file = open("QuizScore.scv", 'r')
for row in file:
    print(row)
file.close()
