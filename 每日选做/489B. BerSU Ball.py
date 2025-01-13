n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
a.sort()
b.sort()
c=0
for i in a:
    for j in b:
        #abs绝对值
        if i==j-1:
            b.remove(j)
            c+=1
            break
        elif i== j:
            b.remove(j)
            c += 1
            break
        elif i==j+1:
            b.remove(j)
            c+=1
            break
print(c)