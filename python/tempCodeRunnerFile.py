list = {}
for i in range(4):
    name = input("name: ")
    age = int(input("age: "))
    shoesize=int(input("shoe size: "))
    list[name] ={"Age": age, "ShoeSize":shoesize}
name = input("Enter a name you want to delete: ")
del list[name]

for name in list:
    print(name, list[name])