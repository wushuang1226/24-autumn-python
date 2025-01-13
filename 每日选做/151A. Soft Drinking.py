a=list(map(int,input().split()))
n=a[0]
k=a[1]
l=a[2]
c=a[3]
d=a[4]
p=a[5]
nl=a[6]
np=a[7]
#简写n, k, l, c, d, p, nl, np = map(int, input().split())
print(int(min(k*l/nl,c*d,p/np)/n))
#15min
