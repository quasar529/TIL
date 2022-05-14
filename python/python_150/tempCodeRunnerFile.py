
cccp=0
ccwp=0
data1 = ('a','b','c','d')
data2=('a','c','e','f')
for i ,j  in zip(data1,data2):
    if i == j:
        cccp += 1
    elif i in data2:
        ccwp += 1
        
print(cccp,ccwp)