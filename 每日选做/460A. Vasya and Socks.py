n,m=map(int,input().split())
d=0
while True:
    if n==0:
        break
    n-=1
    d+=1
    if d%m==0:
        n+=1
print(d)
