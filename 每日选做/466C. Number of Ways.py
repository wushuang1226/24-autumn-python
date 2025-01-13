#双指针不一定是一左一右
n = int(input())
a = [int(i) for i in input().split()]
s = sum(a)
x = 0
if s%3 == 0:#剪枝不整除
    d1 = s/3
    d2 = 2*d1
    z = t = 0
    for i in range(n-1):
        z += a[i]

        if z == d2:
            x += t#加上在其左边的三分之一
        if z == d1:
            t += 1
print(x)