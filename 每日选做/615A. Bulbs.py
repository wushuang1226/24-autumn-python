n,m=map(int,input().split())
b=set()
for i in range(n):

    a=list(map(int, input().split()))
    a.remove(a[0])
    for j in a:
        b.add(j)
    #b.update(input().split()[1:])

for i in range(1,m+1):
    if i not in b:
        print("NO")
        break
        #"for else"用法要加break！
else:
    print("YES")
#print(['NO','YES'][len(b)==m])
