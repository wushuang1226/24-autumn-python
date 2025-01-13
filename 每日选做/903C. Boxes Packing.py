import bisect
n=int(input())
a=list(map(int,input().split()))
a.sort()
v=[1]*n
b=a[::]
c=0
for i in range(n):
    point=bisect.bisect_right(b,a[i])
    if point==len(b):
        break
    else:
        b.pop(point)
        c+=1
print(n-c)

'''贪心——统计数量最多同一大小的箱子？！
from collections import *
input()
print(max(Counter(input().split()).values()))'''