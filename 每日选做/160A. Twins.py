n=int(input())
a=list(map(int,input().split()))
#a=[int(i) for i in input().split()]（给split一个输出途径）
b=list()
k=sum(a)
while True:
    b.append(max(a))
    a.remove(max(a))
    if sum(b)>k/2:
        break
print(len(b))
#a.sort()顺序取即可

    
