# Tkinter GUI

import csv
from pathlib import WindowsPath
import random
from asyncio import _enter_task
from dbm import whichdb
from email import message
from functools import total_ordering
import imp
from multiprocessing.connection import answer_challenge
from re import T
from tkinter import *
from turtle import clear

from matplotlib.pyplot import text


def Call():
    msg = Label(window, text="You pressed the button")
    msg.place(x=30, y=50)
    button["bg"] = "blue"
    button["fg"] = "white"


window = Tk()
window.geometry("200x100")
button = Button(text="Press me", command=Call)
button.place(x=30, y=20, width=120, height=25)
window.mainloop()


window = Tk()
window.title("Window title")
window.geometry("450x100")
label = Label(text="Enter number:")
entry_box = Entry(text=0)
output_box = Message(text=0)
output_box["bg"] = "red"
output_box["fg"] = "white"
output_box["relief"] = "sunken"
list_box = Listbox()
entry_box["justify"] = "center"
button1 = Button(text="Click here", command=click)
label.place(x=50, y=20, width=100, height=25)
entry_box.delete(0, END)
num = entry_box.get()
answer = output_box["text"]
output_box["text"] = total_ordering
window.mainloop()
# 124


def click():
    name = textbox1.get()
    message = str("Hello "+name)
    textbox2["bg"] = "yellow"
    textbox2["fg"] = "blue"
    textbox2["text"] = message


window = Tk()
window.geometry("500x200")

label1 = Label(text="Enter your name: ")
label1.place(x=30, y=20)

textbox1 = Entry(text="")
textbox1.place(x=150, y=20, width=200, height=25)
textbox1["justify"] = "center"
textbox1.focus()

button1 = Button(text="Press me", command=click)
button1.place(x=30, y=50, width=120, height=25)

textbox2 = Message(text="", width=200)
textbox2.place(x=150, y=50, width=200, height=25)
textbox2["bg"] = "white"
textbox2["fg"] = "black"
window.mainloop()

# 125


def click():
    num = random.randint(1, 6)
    answer["text"] = num


window = Tk()
window.title("Roll a dice")
window.geometry("100x120")
button1 = Button(text="Roll", command=click)
button1.place(x=30, y=30, width=50, height=25)

answer = Message(text="")
answer.place(x=40, y=70, width=30, height=25)

window.mainloop()

# 126


def add():
    num = enter_txt.get()
    num = int(num)
    answer = output_txt["text"]
    answer = int(answer)
    total = num+answer
    output_txt["text"] = total


def reset():
    output_txt["text"] = 0


window = Tk()
window.title("Adding together")
window.geometry("450x100")

enter_lbl = Label(text="Enter a number: ")
enter_lbl.place(x=50, y=20, width=100, height=25)

enter_txt = Entry(text=0)
enter_txt.place(x=150, y=20, width=100, height=25)
enter_txt["justify"] = "center"
enter_txt.focus()

add_btn = Button(text="Add", command=add)
add_btn.place(x=300, y=20, width=50, height=25)

output_lbl = Label(text="Anwser: ")
output_lbl.place(x=50, y=50, width=100, height=25)

output_txt = Message(text=0)
output_txt.place(x=150, y=50, width=100, height=25)
output_txt["bg"] = "white"
output_txt["relief"] = "sunken"

reset_btn = Button(text="Reset", command=reset)
reset_btn.place(x=300, y=50, width=50, height=25)

window.mainloop()

# 127


def add_name():
    name = name_box.get()
    name_list.insert(END, name)
    name_box.delete(0, END)
    name_box.focus()


def clear_list():
    name_list.delete(0, END)
    name_box.focus()


window = Tk()
window.title("Names List")
window.geometry("450x100")

label1 = Label(text="Enter a name: ")
label1.place(x=20, y=20, width=100, height=25)

name_box = Entry(text=0)
name_box.place(x=120, y=20, width=100, height=25)
name_box.focus()

add_btn = Button(text="add name", command=add_name)
add_btn.place(x=250, y=20, width=100, height=25)

name_list = Listbox()
name_list.place(x=120, y=50, width=100, height=100)

clear_btn = Button(text="Clear list", command=clear_list)
clear_btn.place(x=250, y=50, width=100, height=25)


window.mainloop()

# 128


def mileToKilo():
    mile = textbox1.get()
    mile = float(mile)
    message = mile*1.6093
    textbox2.delete(0, END)
    textbox2.insert(END, message)
    textbox2.insert(END, "km")


def kiloToMile():
    kilo = textbox1.get()
    kilo = float(kilo)
    message = kilo*0.6214
    textbox2.delete(0, END)
    textbox2.insert(END, message)
    textbox2.insert(END, "mile")


window = Tk()
window.title("Mile Kilo changer")
window.geometry("450x200")

label1 = Label(text="Enter a value you want to convert ")
label1.place(x=20, y=20)

textbox1 = Entry(text=0)
textbox1.place(x=30, y=50, width=200, height=25)
textbox1["justify"] = "center"
textbox1.focus()

button1 = Button(text="Miles to Kilo", command=mileToKilo)
button1.place(x=30, y=80, width=200, height=25)

button2 = Button(text="Kilo to mile", command=kiloToMile)
button2.place(x=30, y=110, width=200, height=25)

textbox2 = Entry(text=0)
textbox2.place(x=30, y=140, width=200, height=25)
textbox2["justify"] = "center"

window.mainloop()

# 129


def add_number():
    num = textbox1.get()
    if num.isdigit():
        num_list.insert(END, num)
        textbox1.delete(0, END)
        textbox1.focus()
    else:
        textbox1.delete(0, END)
        textbox1.focus()


def clear_list():
    num_list.delete(0, END)
    textbox1.focus()


window = Tk()
window.title("Number List ")
window.geometry("450x200")

label1 = Label(text="Enter a Number: ")
label1.place(x=20, y=20)

textbox1 = Entry(text=0)
textbox1.place(x=120, y=20, width=100, height=25)
textbox1["justify"] = "center"
textbox1.focus()

button1 = Button(text="Add to list: ", command=add_number)
button1.place(x=250, y=20, width=100, height=25)

num_list = Listbox()
num_list.place(x=120, y=50, width=100, height=100)

button2 = Button(text="Delete a num", command=clear_list)
button2.place(x=250, y=50, width=100, height=25)

window.mainloop()

# 130


def add_number():
    num = textbox1.get()
    if num.isdigit():
        num_list.insert(END, num)
        textbox1.delete(0, END)
        textbox1.focus()
    else:
        textbox1.delete(0, END)
        textbox1.focus()


def clear_list():
    num_list.delete(0, END)
    textbox1.focus()


window = Tk()
window.title("Number List ")
window.geometry("450x200")

label1 = Label(text="Enter a Number: ")
label1.place(x=20, y=20)

textbox1 = Entry(text=0)
textbox1.place(x=120, y=20, width=100, height=25)
textbox1["justify"] = "center"
textbox1.focus()

button1 = Button(text="Add to list: ", command=add_number)
button1.place(x=250, y=20, width=100, height=25)

num_list = Listbox()
num_list.place(x=120, y=50, width=100, height=100)

button2 = Button(text="Delete a num", command=clear_list)
button2.place(x=250, y=50, width=100, height=25)

window.mainloop()

# 131


def createAFile():
    file = open("ages.csv", 'w')
    file.close()


def save_list():
    file = open("ages.csv", 'a')
    name = namebox.get()
    age = agebox.get()

    newRecord = name+','+age+'\n'
    file.write(str(newRecord))
    file.close()

    namebox.delete(0, END)
    agebox.delete(0, END)
    namebox.focus()


window = Tk()
window.title("Make csv of name and age")
window.geometry("450x200")

label1 = Label(text="Enter a name")
label1.place(x=20, y=20)

namebox = Entry(text="")
namebox.place(x=120, y=20, width=100, height=25)
namebox["justify"] = "left"
namebox.focus()

label2 = Label(text="Enter a age")
label2.place(x=20, y=50)

agebox = Entry(text="")
agebox.place(x=120, y=50, width=100, height=25)
agebox["justify"] = "left"

button1 = Button(text="Create a File", command=createAFile)
button1.place(x=250, y=20, width=100, height=25)

button2 = Button(text="Add to file", command=save_list)
button2.place(x=250, y=50, width=100, height=25)
window.mainloop()


# 132


def add_file():
    file = open("ages.csv", 'a')
    name = namebox.get()
    age = agebox.get()
    newRecord = name+','+age+'\n'
    file.write(str(newRecord))
    file.close()
    namebox.delete(0, END)
    agebox.delete(0, END)
    namebox.focus()


def read_file():
    name_list.delete(0, END)

    file = open("ages.csv", 'r')
    tmp = []
    for row in file:
        tmp.append(row)
    for data in tmp:
        name_list.insert(END, data)


window = Tk()
window.title("Name List")
window.geometry("450x200")

label1 = Label(text="Enter a name")
label1.place(x=20, y=20)

namebox = Entry(text="")
namebox.place(x=120, y=20, width=100, height=25)
namebox["justify"] = "left"
namebox.focus()

label2 = Label(text="Enter a age")
label2.place(x=20, y=50)

agebox = Entry(text="")
agebox.place(x=120, y=50, width=100, height=25)
agebox["justify"] = "left"

button1 = Button(text="Add to file", command=add_file)
button1.place(x=250, y=20, width=100, height=25)

button2 = Button(text="Read a list", command=read_file)
button2.place(x=250, y=50, width=100, height=25)

label3 = Label(text="Saved names: ")
label3.place(x=250, y=80)

name_list = Listbox()
name_list.place(x=120, y=80, width=230, height=100)

window.mainloop()
