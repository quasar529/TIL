
import csv
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
