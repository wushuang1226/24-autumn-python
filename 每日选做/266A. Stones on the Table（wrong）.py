#剩了多少个石头…
n=int(input())
a=list(input())
b=list()
for i in range(n-1):
        if a[i]==a[i+1]:
            b.append(i)
for j in b:
    a.remove(a[j])
    for x in range(len(b)):
        b[x]=b[x]-1
print(len(a))
