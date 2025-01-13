n=int(input())
b=list(map(int,input().split()))
a=[x for x in range(1,n+1)]
c=[]
for i in b:
    if i in a:
        a.remove(i)
    else:
        c.append(i)
#original_class = set(range(1, n + 1))
#missing_children = sorted(original_class - remaining_set)
#集合的差运算
a.sort()
a=[str(i) for i in a]
print(' '.join(a))
c.sort()
c=[str(i) for i in c]
print(' '.join(c))
