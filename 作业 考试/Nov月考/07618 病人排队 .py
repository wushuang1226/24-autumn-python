#20min uwuwuwuwuwu
n=int(input())
a=[]
b=[]
c=[]
for i in range(n):
    a.append(list(input().split()))
for i in a:
    i[1]=int(i[1])
for i in a:
    if i[1]>=60:
        b.append(i)
    else:
        c.append(i)
b.sort(key=lambda x:x[1],reverse=True)
#登记顺序不等于ID顺序！！这是sorting第一题！！
for i in b+c:
    print(i[0])