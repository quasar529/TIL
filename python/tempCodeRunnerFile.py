
names=[]
def add_name():
    name= input("NAME:? ")
    names.append(name)
    return names

def show_name():
    x=0
    for name in names:
        print(x,' ',name)
        x+=1
    print('\n')

def modify_name():
    show_name()
    user =int(input("Which name you want to modify? choose index: "))
    newName = input("New Name: ")
    names[user] =newName
    return names

def del_name():
    show_name()
    user =int(input("Which name you want to delete? choose index: "))
    del names[user]
    return names

def main():
    while 1:    
        user = int(input("Menu\n1)add\n2)modify\n3)delete\n4)show\n5)END\n"))
        if user==1:
            add_name()
        elif user==2:
            modify_name()
        elif user ==3:
            del_name()
        elif user==4:
            show_name()
        elif user ==5:
            break
        
main()