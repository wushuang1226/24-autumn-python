n=int(input())
a=0
for i in range(n):
    i=list(map(int,input().split()))
    if sum(i)>=2:
        a=a+1
    else:
        pass
print(a)
