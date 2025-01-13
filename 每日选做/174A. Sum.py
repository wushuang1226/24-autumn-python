n=int(input())
for i in range(n):
    a=list(map(int,input().split()))
    x=max(a)
    a.remove(x)
    if x==sum(a):
        print("YES")
    else:
        print("NO")
#sort排序
