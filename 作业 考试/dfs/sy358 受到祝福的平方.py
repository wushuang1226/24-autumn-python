import math
A=input()
c=0#多分支辅助标记结果  优于return只能一次

def dfs(a):
    global c
    if math.sqrt(int(a))%1==0 and int(a)!=0:#00000
        c=1
    l=1
    while l<len(a):
        if math.sqrt(int(a[:l]))%1==0:
            dfs(a[l:])
        l+=1

dfs(A)
if c:
    print("Yes")
else:
    print("No")


