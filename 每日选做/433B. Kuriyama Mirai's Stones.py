#前缀和 类dp记忆
n=int(input())
v=list(map(int,input().split()))
u=sorted(v)
m=int(input())
prev=[v[0]]+[0]*(n-1)
preu=[u[0]]+[0]*(n-1)
for i in range(1,n):
    prev[i]=prev[i-1]+v[i]
    preu[i]=preu[i-1]+u[i]
#print(prev,preu)
for i in range(m):
    t,l,r=map(int,input().split())
    if t==1:
        if l==1:#开头！！
            print(prev[r-1])
        else:
            print(prev[r-1]-prev[l-2])
    else:
        if l==1:
            print(preu[r-1])
        else:
            print(preu[r-1]-preu[l-2])
