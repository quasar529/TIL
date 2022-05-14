# 96
arr = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
print(arr)

# 97
row = int(input("Row: "))
col = int(input("Col: "))
print(arr[row][col])

# 98
arr = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]

row = int(input("row: "))
print(arr[row])
user = int(input("new val: "))
arr[row].append(user)
print(arr)

# 99
arr = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]

row = int(input("row: "))
print(arr[row])
col = int(input("col :"))
print(arr[row][col])
user = input("y or n? ")
if user == 'y':
    newval = int(input("new val?"))
    arr[row][col] = newval
    print(arr[row])

# 100
dict = {"John": {"N": 3056, "S": 8463, "E": 8441, "W": 2684},
        "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
        "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
        "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451}}
print(dict)

# 101
dict = {"John": {"N": 3056, "S": 8463, "E": 8441, "W": 2684},
        "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
        "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
        "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451}}
print(dict)
name = input("name: ")
place = input("place")
print(dict[name][place])

changeval = int(input("enter: "))
dict[name][place] = changeval
print(dict[name])

# 102
list = {}
for i in range(4):
    name = input("name: ")
    age = int(input("age: "))
    shoesize = int(input("shoe size: "))
    list[name] = {"Age": age, "Shoe Size": shoesize}
name = input("Enter one of them: ")
print(list[name])

# 103
list = {}
for i in range(4):
    name = input("name: ")
    age = int(input("age: "))
    shoesize = int(input("shoe size: "))
    list[name] = {"Age": age, "ShoeSize": shoesize}

for name in list:
    print(name, list[name]["ShoeSize"])

# 104
list = {}
for i in range(4):
    name = input("name: ")
    age = int(input("age: "))
    shoesize = int(input("shoe size: "))
    list[name] = {"Age": age, "ShoeSize": shoesize}
name = input("Enter a name you want to delete: ")
del list[name]

for name in list:
    print(name, list[name])
