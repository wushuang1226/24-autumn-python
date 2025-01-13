a=list(map(int,input().split()))
#n,m=map...
n=a[0]
m=a[1]
b=list(map(int,input().split()))
y=0
for i in range(m):
    x=min(b)
    if x<0:
        b.remove(x)
        y=y-x
    else:
        break
print(y)

    
