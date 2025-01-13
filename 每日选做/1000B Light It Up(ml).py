#直接做超超超
n,m=map(int,input().split())
a=[0]+list(map(int,input().split()))+[m]

def lit(a):
    l=0
    for i in range(len(a)-1):
        if i%2==0:
            l+=a[i+1]-a[i]
    return l

b={i for i in range(m+1)}
a0=set(a)
b0=b-a0
a0.clear()
c=[lit(a)]
for i in b0:
    l=lit(a)
    a1=tuple(a)
    a2=list(a1)
    a2.append(i)
    a2.sort()
    c.append(lit(a2))
print(max(c))