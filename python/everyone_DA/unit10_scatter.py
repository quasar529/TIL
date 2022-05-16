import random
import matplotlib.pyplot as plt
from cProfile import label
import csv
import imp
f = open('everyone_DA\gender.csv')
data = csv.reader(f)
male = []
female = []
name = input('궁금한 동네 입력 ')
# for row in data:
#     if name in row[0]:
#         for i in range(3, 104):
#             male.append(int(row[i].replace(',', '')))
#             female.append(int(row[i+103].replace(',', '')))
#         break


# plt.rc('font', family='Malgun Gothic')
# plt.plot(male, label='Male')
# plt.plot(female, label='Female')
# plt.legend()
# plt.show()


# result = []
# for row in data:
#     if name in row[0]:
#         for i in range(3, 104):
#             result.append(int(row[i].replace(',', '')) -
#                           int(row[i+103].replace(',', '')))
#         break

# plt.bar(range(101), result)
# plt.show()

# plt.scatter([1, 2, 3, 4], [10, 30, 20, 40], s=[
#             100, 300, 500, 700], c=range(4), cmap='jet')

# plt.colorbar()
# plt.show()


# x = []
# y = []
# size = []
# for i in range(100):
#     x.append(random.randint(1, 500))
#     y.append(random.randint(1, 500))
#     size.append(random.randint(100, 500))

# plt.scatter(x, y, c=range(100), s=size, cmap='jet', alpha=0.5)
# plt.colorbar()
# plt.show()


for row in data:
    if name in row[0]:
        for i in range(3, 104):
            male.append(int(row[i].replace(',', '')))
            female.append(int(row[i+103].replace(',', '')))
        break

plt.scatter(male, female, c=range(101), cmap='jet', alpha=0.7)
plt.colorbar()
plt.plot(range(max(male)), range(max(male)), 'g')
plt.show()
