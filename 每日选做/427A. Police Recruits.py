n=int(input())
a=list(map(int,input().split()))
b=0
c=0
for i in range(n):
#for i in a:
    if a[i]>0:
        b=b+a[i]
    else:
        if b>0:
            b=b-1
            #b-=1
        else:
            c=c+1
print(c)
