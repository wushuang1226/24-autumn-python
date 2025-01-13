p=int(input())
a=list(map(int,input().split()))
#先排序咧
a.sort()
b=0
c=0
d=[]
#two pointers
#先买便宜的，先卖贵的
x=0
y=len(a)-1
while True:
    if x>y:
        d.append(b-c)
        print(max(d))
        break
    if b<=c and p<a[x]:
        d.append(b - c)
        print(max(d))
        break

    elif p>=a[x]:
        p-=a[x]
        b+=1
        x+=1
    else:
        p+=a[y]
        d.append(b - c)
        c+=1
        y-=1

