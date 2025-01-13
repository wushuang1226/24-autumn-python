n,k=map(int,input().split())
#学习了一下双指针算法~
a=list(map(int,input().split()))
b=0
i=0
j=n-1
while i<j:
    #分支写成一个 要不然容易有差错
    if a[i]+a[j]<k:
        i+=1
    elif a[i]+a[j]>k:
        j-=1
    else:
        b+=1
        print(i,j)
        i+=1
print(b)

