
from tkinter import *
import csv

def add_file():
    file = open("ages.csv",'a')
    name= namebox.get()
    age=agebox.get()
    newRecord = name+','+age+'\n'
    file.write(str(newRecord))
    file.close()
    namebox.delete(0,END)
    agebox.delete(0,END)
    namebox.focus()

def read_file():
    name_list.delete(0,END)
    
    file=open("ages.csv",'r')
    tmp=[]
    for row in file:
        tmp.append(row)
    for data in tmp:
        name_list.insert(END,data)

window=Tk()
window.title("Name List")
window.geometry("450x200")

label1=Label(text="Enter a name")
label1.place(x=20,y=20)

namebox = Entry(text="")
namebox.place(x=120,y=20,width=100,height=25)
namebox["justify"] ="left"
namebox.focus()

label2 = Label(text="Enter a age")
label2.place(x=20,y=50)

agebox = Entry(text="")
agebox.place(x=120,y=50,width=100,height=25)
agebox["justify"]="left"

button1 = Button(text = "Add to file",command=add_file)
button1.place(x=250,y=20,width=100,height=25)

button2=Button(text="Read a list",command=read_file)
button2.place(x=250,y=50,width=100,height=25)

label3=Label(text="Saved names: ")
label3.place(x=250,y=80)

name_list = Listbox()
name_list.place(x=120,y=80,width=230,height=100)

window.mainloop()