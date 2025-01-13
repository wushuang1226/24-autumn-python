n=int(input())
a=list(map(int,input().split()))
K=int(input())
b=0
for i in a:
    if K-i in a:
        b+=1/2
print(int(b))