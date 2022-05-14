import random

colors = ["r", "b", "o", "y", "p", "g", "w"]


def select_colors():
    c1 = random.choice(colors)
    c2 = random.choice(colors)
    c3 = random.choice(colors)
    c4 = random.choice(colors)
    data = (c1, c2, c3, c4)
    return data


def get_colors():
    print(colors, "Enter 4 colors with a space, only in lower!")
    while 1:
        c1 = input("1st color: ")
        if c1 in colors:
            print("Great pick next color: ")
            break
        else:
            print("Your input is wrong, try again!")
    while 1:
        c2 = input("2nd color: ")
        if c2 in colors:
            print("Great pick next color: ")
            break
        else:
            print("Your input is wrong, try again!")
    while 1:
        c3 = input("3rd color: ")
        if c3 in colors:
            print("Great pick next color: ")
            break
        else:
            print("Your input is wrong, try again!")
    while 1:
        c4 = input("4th color: ")
        if c4 in colors:
            print("Great pick next color: ")
            break
        else:
            print("Your input is wrong, try again!")

    data = (c1, c2, c3, c4)

    return data


def judgeRorW(data1, data2):
    cccp = 0
    ccwp = 0
    for i, j in zip(data1, data2):
        if i == j:
            cccp += 1
        elif j in data1:
            ccwp += 1
    return cccp, ccwp


def main():
    print(colors)
    cccp, ccwp = judgeRorW(('r', 'b', 'r', 'g'), get_colors())
    print("Correct color in the correct place:", cccp,
          'Correct color but in the wrong place:', ccwp)


main()
# cccp=0
# ccwp=0
# data1 = ('a','b','c','d')
# data2=('a','c','e','f')
# for i ,j  in zip(data1,data2):
#     if i == j:
#         cccp += 1
#     elif i in data2:
#         ccwp += 1

# print(cccp,ccwp)
