n=int(input())
a={'4','7'}
#int or str!!
for i in range(1,n+1):
    if n%i==0:
        if set(str(i)).issubset(a):
            #if s.count('4') + s.count('7') == len(s):
            print("YES")
            break
else:
    print("NO")

'''函数判断
def check(x):
    s = str(x)
    法一
    for c in s:
        if c!= '4' and c!= '7':
            return False
    return True
    法二（一一对应）
    return [False, True][s.count('4') + s.count('7') ==len(s)]
    只会有一个返回值'''