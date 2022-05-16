import csv
from turtle import st
import matplotlib.pyplot as plt

f = open('everyone_DA\gender.csv')
data = csv.reader(f)
# male = []
# female = []
place = input("찾고 싶은 지역 입력: ")
# for row in data:
#     if place in row[0]:
#         for i in row[3:104]:
#             male.append(-int(i.replace(',', '')))
#         for i in row[106:]:
#             female.append(int((i.replace(',', ''))))
#         break
# plt.style.use('ggplot')
# plt.title(place+' 지역의 성별 인구 분포')
# plt.figure(figsize=(10, 5), dpi=300)
# plt.rc('font', family='Malgun Gothic')
# plt.rcParams['axes.unicode_minus'] = False
# plt.barh(range(101), male, label='남성')
# plt.barh(range(101), female, label='여자')
# plt.legend()
# plt.show()

# plt.rc('font', family='Malgun Gothic')
# label = ['A', 'B', 'O', 'AB']
# color = ['r', 'orange', 'y', 'g']
# plt.pie([2441, 2312, 1220, 1111], labels=label,
#         autopct='%.1f%%', colors=color, explode=(0, 0, 0, 0.1))
# plt.axis('equal')
# plt.show()

size = []
for row in data:
    if place in row[0]:
        male = 0
        female = 0
        for i in range(101):
            male += int(row[i+3].replace(',', ''))
            female += int(row[i+106].replace(',', ''))
        break
size.append(male)
size.append(female)
print(size)

plt.rc('font', family='Malgun Gothic')
color = ['crimson', 'darkcyan']
plt.axis('equal')
plt.pie(size, labels=['남', '여'], autopct='%.1f%%', colors=color, startangle=90)
plt.title(place+' 지역의 성별 비율')
plt.show()
