#一个要求？
while True:
    n=int(input())
    if n==0:
        break
    a=[]
    for i in range(n):
        a.append(tuple(map(int,input().split())))
    a.sort(key=lambda x:(x[0],x[1]))
    min_price=a[0][1]
    c=1
    for i in range(n):
        if a[i][1]<min_price:
            c+=1
            min_price=a[i][1]
    #print(a)
    print(c)
