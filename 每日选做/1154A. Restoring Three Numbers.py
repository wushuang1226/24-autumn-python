n=list(map(int,input().split()))
x=max(n)
n.remove(x)
x1=n[0]
x2=n[1]
x3=n[2]
print(x-x1,x-x2,x-x3,end=" ")
#sort()默认升序
