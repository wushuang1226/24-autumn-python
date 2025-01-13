#查找了分解因式的答案
n=int(input())

#找因数务必二分法！
'''
a=2
b=[]
while True:
    if a==n:
        b.append(a)
        break
    elif n%a==0:
        n=n/a
        b.append(a)
    else:
        a+=1'''
def pFactors(n):
    """Finds the prime factors of 'n'"""
    from math import sqrt
    p, limit, check, num = [], int(sqrt(n)) + 1, 2, n

    for check in range(2, limit):
        if check >n:
            break
        while num % check == 0:
            p.append(check)
            num /= check
    if num > 1:#对于质数
        p.append(num)
    return p

b=pFactors(n)
d=set(b)
if len(b)>len(d):
    x=0
elif len(d)%2==0:#0_False
    x=1
else:
    x=-1

print(x)


