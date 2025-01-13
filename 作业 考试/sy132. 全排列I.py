#类似八皇后,逐个位置构造排列
list1=[]

def s(a,n):
    if len(a)==n:
        list1.append(a)
        return
    else:
        for i in range(1,n+1):
            if i not in a:
                s(a+[i],n)

n=int(input())
s([],n)
for i in list1:
    print(*i )
