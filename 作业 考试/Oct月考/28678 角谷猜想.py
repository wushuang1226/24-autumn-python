#这个做过
#5min
n=int(input())
while n!=1:
    if n%2==1:
        a=n
        n=n*3+1
        print('%d*3+1=%d'%(a,n))
    else:
        a=n
        n/=2
        print('%d/2=%d'%(a,n))
print("End")

