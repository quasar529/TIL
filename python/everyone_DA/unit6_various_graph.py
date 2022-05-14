import csv
import random
import matplotlib.pyplot as plt
plt.hist([1, 1, 2, 3, 4, 5, 6, 7, 8, 9])
plt.show()

dice = []
for i in range(100000):
    dice.append(random.randint(1, 6))
plt.hist(dice, bins=6)
plt.show()


f = open('everyone_DA\seoul.csv')
data = csv.reader(f)
next(data)
august = []
janu = []
for row in data:
    if row[-1] != '':
        if row[0].split('-')[1] == '08':
            august.append(float(row[-1]))
        elif row[0].split('-')[1] == '01':
            janu.append(float(row[-1]))
plt.hist(august, bins=100, color='r')
plt.hist(janu, bins=100, color='b')
plt.show()

result = []
for i in range(15):
    result.append(random.randint(1, 1000))
print(sorted(result))
plt.boxplot(result)
plt.show()

f = open('everyone_DA\seoul.csv')
data = csv.reader(f)
next(data)
aug = []
jan = []
for row in data:
    if row[-1] != '':
        if row[0].split('-')[1] == '01':
            jan.append(float(row[-1]))
        elif row[0].split('-')[1] == '08':
            aug.append(float(row[-1]))
plt.boxplot(jan)
plt.boxplot(aug)
plt.show()
plt.boxplot([aug, jan])
plt.show()

month = [[], [], [], [], [], [], [], [], [], [], [], []]

for row in data:
    if row[-1] != '':
        month[int(row[0].split('-')[1])-1].append(float(row[-1]))
plt.boxplot(month)
plt.show()

day = []
for i in range(31):
    day.append([])

for row in data:
    if row[-1] != '':
        if row[0].split('-')[1] == '08':
            day[int(row[0].split('-')[2])-1].append(float(row[-1]))
plt.style.use('ggplot')
plt.figure(figsize=(10, 5), dpi=300)
plt.boxplot(day, showfliers=False)
plt.show()
