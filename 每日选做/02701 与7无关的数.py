n=int(input())
a=[x for x in range(n+1)]
for i in range(n+1):
    if i %7==0:
        a.remove(i)
        continue
    b=str(i)
    for j in b:
        if j=='7':
            a.remove(i)
print(sum([x**2 for x in a]))
#中括号可以去掉，也可以def一个函数return True/False


            
    
