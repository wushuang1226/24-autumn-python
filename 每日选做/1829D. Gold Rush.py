
from functools import lru_cache
@lru_cache(maxsize=None)
def dfs(x,y):
    #print(x,y)
    global ans
    if x==y:
        return True
    elif x%3!=0 or x<y:
        return False
    if dfs(2 * x / 3, y):
        return True#递归的写法！
    if dfs(x/3,y):
        return True

t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    if dfs(n,m):
        print("YES")
    else:
        print("NO")

