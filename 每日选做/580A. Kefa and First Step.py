n=int(input())
a=list(map(int,input().split()))
b=1
c=[]
for i in range(len(a)-1):
    if a[i]>a[i+1]:
        c+=[b]
        b=1
    else:
        b+=1
c+=[b]
print(max(c))
    
    
