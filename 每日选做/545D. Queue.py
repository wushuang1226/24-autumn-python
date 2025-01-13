n=int(input())
a=list(map(int,input().split()))
a.sort()
pre=0
c=0
for i in range(n):
    '''完全遍历的错解！！
    a0=a[i]
    print(pre,a0)
    if pre>a0:
        c+=1
    pre+=a0'''
    #print(pre,a[i])
    if a[i]>=pre:
        pre+=a[i]#失望的人无需在前面接受服务，因为无论如何也要失望！
        c+=1
print(c)