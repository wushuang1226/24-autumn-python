#相等的特殊情况
import bisect#二分搜索优化
n=int(input())
a=list(map(int,input().split()))
b=[a[0]]
c=1
for i in range(1,n):
    #print(b)
    if a[i]<b[0]:
        b.insert(0,a[i])
        c+=1
    elif a[i]>=b[-1]:
        b[-1]=a[i]
    else:
        k=bisect.bisect_right(b,a[i])#想清楚哪边&取等啊啊
        b[k]=a[i]
print(c)




