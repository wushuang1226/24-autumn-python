n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=a+b
c.sort()
c0=[str(i)for i in c]
print(' '.join(c0))