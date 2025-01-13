n=int(input())
a=list(map(int,input().split()))
if a[0]%2!=a[1]%2 and a[0]%2!=a[2]%2:
    print(1)
elif a[n-1]%2!=a[n-2]%2 and a[n-1]%2!=a[n-3]%2:
    print(n)
for i in range(n-2):
    if a[i]%2!=a[i+1]%2 and a[i+1]%2!=a[i+2]%2:
        print(i+2)
        break
'''法二：计数偶数个数，1个还是多个
print(a.index(1) + 1)查找
a = [i % 2 for i in a]列表推导式

