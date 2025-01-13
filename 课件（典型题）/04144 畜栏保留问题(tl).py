n=int(input())
a=[]
t=[]
b=[0]*n
for i in range(n):
    #编号后排序
    a.append(list(map(int,input().split()))+[i])
a.sort()
t.append(a[0][1])
b[0]=1
for i in range(1,n):
    if a[i][0]>min(t):
        t0=t.index(min(t))
        t[t0]=a[i][1]
        b[a[i][2]]=t0+1
        #有更新
    else:
        t.append(a[i][1])
        b[a[i][2]]=t.index(a[i][1])+1
        #print(t,b)
print(len(t))
for i in b:
    print(i)

