#时间短的先做
n=int(input())
b=list(map(int,input().split()))
a=[[b[i],i] for i in range(n)]
a.sort()
c=[str(i[1]+1)for i in a]
d=0
for i in range(n):
    d+=a[i][0]*(n-i-1)
    #都排序啦就别再用b啦
print(' '.join(c))
print(f'{d/n:.2f}')
#一遍AC啦 这道不难

