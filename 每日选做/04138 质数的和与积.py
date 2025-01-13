#离得最近积最大?4
is_prime=[True]*(10001)
is_prime[1]=False
primes=[]
for i in range(2,10000+1):
    if is_prime[i]:
        primes.append(i)
    for p in primes:
        if i*p>10000:
            break
        is_prime[i*p]=False
        if i%p==0:
            break
#print(primes)
n=int(input())
import bisect
if n%2==0 and is_prime[int(n/2)]:
    print(int(n**2/4))#float与int！！
else:
    point=bisect.bisect(primes,n/2)
    #print(point)
    for i in range(point-1,-1,-1):
        p1=primes[i]
        if is_prime[n-p1]:
            print(int(p1*(n-p1)))
            break
'''可以遍历完全，不是很大
maxmultiple = 0
f = 2
while f<S:
    if isprime(S - f):
        maxmultiple = max(maxmultiple, f*(S-f))
    f += 1
    while isprime(f)==False:##while循环
        f += 1
'''