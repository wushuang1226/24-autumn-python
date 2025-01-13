import math

for x in range(5):
    i=list(map(int,input().split()))
    if sum(i)==1:
        a=x
        break
for y in range(5):
    if i[y]==1:
        b=y
c=math.fabs(a-2)+math.fabs(b-2)
print(int(c))
#20min
#abs绝对值
'''better:
matrix = [[int(x) for x in input().split()] for i in range(5)]
列表矩阵建立方法
for i in range(5):
    if 1 in matrix[i]:
        j = matrix[i].index(1)
        print(abs(i-2)+abs(j-2))
        break'''
