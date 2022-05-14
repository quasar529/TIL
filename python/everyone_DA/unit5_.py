import matplotlib.pyplot as plt
import csv
f = open('everyone_DA\seoul.csv')
data = csv.reader(f)
next(data)
# result = []

# for row in data:
#     if row[4] != '':
#         if row[0].split('-')[1] == '08':
#             result.append(float(row[-1]))
# print(len(result))
# plt.figure(figsize=(10, 2))
# plt.plot(result, 'lightpink')
# plt.show()

birthdaytemphigh = []
birthdaytemplow = []

for row in data:
    if row[-1] != '' and row[-2] != '':
        if row[0].split('-')[1] == '05' and row[0].split('-')[2] == '29':
            birthdaytemphigh.append(float(row[-1]))
            birthdaytemplow.append(float(row[-2]))
print(len(birthdaytemplow))
plt.plot(birthdaytemphigh, 'hotpink', label='high')
plt.plot(birthdaytemplow, 'skyblue', label='low')
plt.legend()
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False
plt.title("My birthday's temperature")
plt.show()
