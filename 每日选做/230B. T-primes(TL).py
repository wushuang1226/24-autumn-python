#先排除 再遍历！(3个 1，n，开方)
import math
def t(x):
    if x in [4,9]:
        return True
    if x**(1/2)%1==0 and x>16 and x%2!=0 and x%3!=0:
        for i in range(2,math.ceil(x**(1/4)+1)):
            if x**(1/2)%i==0:
                break
        else:
    #乘方和乘除优先级相同，要加括号
            return True
    return False

n=int(input())
a=map(int,input().split())
for i in a:
    if t(i):
        print("YES")
    else:
        print("NO")
