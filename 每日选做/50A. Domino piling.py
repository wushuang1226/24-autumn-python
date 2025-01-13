p=list(map(int,input().split()))
if p[0]*p[1]%2==0:
    q=p[0]*p[1]/2
else:
    q=(p[0]*p[1]-1)/2
print(int(q))
