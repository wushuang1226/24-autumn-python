t=int(input())
for _ in range(t):
    n=int(input())
    a0=input().split()
    #可以对一个先排序！再求另一个的最长递减。。
    a=[(int(a0[i]),int(a0[i+1]))for i in range(0,2*n,2)]

    from bisect import bisect_left
    a.sort()
    a1=[a[i][1] for i in range(n)]
    a1.reverse()
    lis=[]
    for i in range(n):
        k=bisect_left(lis,a1[i])
        if k<len(lis):
            lis[k]=a1[i]
        else:
            lis.append(a1[i])
    print(len(lis))