#先左倒，不行右倒，不亏
n=int(input())
a=[[-10e9-1,0]]
c=0
for i in range(n):
    a.append(list(map(int,input().split())))
a.append([a[n-1][0]+10e9+1,0])
#这种首尾特殊不太好，容易出问题c=2，n=1不对，可以利用数据扩写列表
for i in range(n):
    if a[i][1]>=a[i][0]-a[i-1][0]:
        if a[i][1] < a[i+1][0] - a[i ][0]:
            c+=1
            a[i][0]+=a[i][1]
            continue
    if a[i][1]<a[i][0]-a[i-1][0]:
        c+=1
print(c)