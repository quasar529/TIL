import csv
import matplotlib.pyplot as plt

# plt.bar([0, 1, 2, 4, 5, 10], [1, 2, 3, 5, 6, 7])
# plt.show()

# plt.bar(range(6), [0, 1, 2, 3, 4, 5])
# plt.show()

# f = open('everyone_DA\korea_ages.csv')
# data = csv.reader(f)
# next(data)

# result = []
# for row in data:
#     if '관악구 청림' in row[0]:
#         for i in row[3:]:
#             result.append(i)

# plt.bar(range(101), result)
# plt.show()

# plt.barh(range(101), result)
# plt.show()

f = open('everyone_DA\gender.csv')
data = csv.reader(f)

male = []
female = []

for row in data:
    if '관악구 청림' in row[0]:
        for i in range(0, 101):
            male.append(-(int(row[i+3])))
            female.append(int(row[-(i+1)]))

plt.style.use('ggplot')
plt.figure(figsize=(10, 5), dpi=300)
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False
plt.title("관악구 청림동 성별 연령 별 인구 분포")

plt.barh(range(101), male, label='남성')
plt.barh(range(101), female, label='여성')
plt.legend()
plt.show()
