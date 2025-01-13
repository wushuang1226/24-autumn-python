#范围较小可以建立素数表
'''
isPrime = [True]* (n+1)
for i in range(2, n+1):
    if isPrime[i]:
        for j in range(2*i, n+1, i):
            isPrime[j] = False'''
def y(x):
    a=1
    for i in range(2,int(x**(1/2))+1):
        if x%i==0:
            a=0
            break
    if a==1:
        return True
    return False
#1不是质数。

n=int(input())
if n<6 or n%2==1:
    print("Error!")
else:
    for i in range(3,int(n/2)+1):
        if y(i) and y(n-i):
            print("%d=%d+%d"%(n,i,n-i))

