
import csv
import random
name= input("Enter your name: ")
score = 0
rdn1 = random.randint(1,100)
rdn2 =random.randint(1,100)
question1 = str(rdn1)+" + " + str(rdn2)+ " = " 
userans = int(input(question1))
realans = rdn1+rdn2
if realans == userans:
    score+=1

rdn3 = random.randint(100,1000)
rdn4 = random.randint(100,1000)
question2 = str(rdn3)+" + " + str(rdn4)+ " = "
userans2 = int(input(question2))
realans2 = rdn3+rdn4
if realans2 ==userans2:
    score+=1
    
file = open("QuizScore.scv",'w')
newRecord = name+','+(question1)+','+str(userans)+','+(question2)+','+str(userans2)+','+str(score)
file.write(str(newRecord))
file.close()

file = open("QuizScore.scv",'r')
for row in file:
    print(row)
file.close()