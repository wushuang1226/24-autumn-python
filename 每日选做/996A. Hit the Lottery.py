n=int(input())
a=0
while True:
    if n>=100:
        q=n//100
        a=a+q
        n=n-100*q
    elif n>=20:
        q=n//20
        a=a+q
        n=n-20*q
    elif n>=10:
        q=n//10
        a=a+q
        n=n-10*q
    elif n>=5:
        q=n//5
        a=a+q
        n=n-5*q
    else:
        q=n
        a=a+q
        break
print(a)
'''better
denominations = [100, 20, 10, 5, 1]
cnt = 0
for i in denominations:!!!!
    cnt += n // i
    n %= i
重复写的代码 通常可以用循环代替'''
