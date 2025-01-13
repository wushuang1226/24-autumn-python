a=list(map(int,input().split()))
b=a[2]
x=a[0]//b
y=a[1]//b
if a[0]%b==0:
    x=x
else:
    x=x+1
if a[1]%b==0:
    y=y
else:
    y=y+1
print(x*y)
