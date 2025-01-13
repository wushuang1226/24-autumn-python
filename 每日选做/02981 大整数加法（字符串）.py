a=list(input())
b=list(input())
#...题里面都说了 可能有多余的前导零
for i in range(len(a)):
    if int(a[i])!=0:
        #时刻谨记数据类型！！不对的话就print自查
        a=a[i:]
        break
for i in range(len(b)):
    if int(b[i])!=0:
        b=b[i:]
        break


if len(a)<len(b):
    for i in range(len(b)-len(a)):
        a.insert(0,0)
if len(b)<len(a):
    for i in range(len(a) - len(b)):
        b.insert(0,0)
c=[int(a[i])+int(b[i]) for i in range(len(a))]
for i in range(len(a)-1,0,-1):
    if c[i]>9:
        #。。c[i]=0
        c[i]=c[i]-10
        c[i-1]+=1
for i in range(len(a)):
    print(c[i],end='')


