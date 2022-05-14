def get_data():
    data = input("Enter your data: ")
    data = data.lower()
    num = int(input("Enter a num 1-26: "))
    record = (data, num)
    return record


def makeACode(data, num):
    newCode = ""
    for i in data:
        if ord(i)+num > 122:
            tmp = ord(i)+num-26
        else:
            tmp = ord(i)+num
        newCode += chr(tmp)
    print(newCode)


def decodeAMessage(data, num):
    newCode = ""
    for i in data:
        if ord(i)-num < 97:
            tmp = ord(i)-num+26
        else:
            tmp = ord(i)-num
        newCode += chr(tmp)
    print(newCode)


def main():
    while 1:
        user = int(input("1) Make a code\n2) Decode a message\n3) Quit\n"))
        if user == 1:
            data, num = get_data()
            makeACode(data, num)
        elif user == 2:
            data, num = get_data()
            decodeAMessage(data, num)
        elif user == 3:
            break


main()
