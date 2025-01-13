#子序列是删两头得到的，找到最小的两头不是x倍数的删去即可
#前缀和与后缀和
#进一步优化?：找到第一个不是x倍数的数,但好像更慢了？
''' for i in range(a//2+1):
        if A[i] or A[~i]:
            s = a-i-1
            break'''
def prefix(a):
    global x,n
    pre_num=1
    for i in range(n):#二分
        #if prefix%x!=0:
        if a[i]!=0:
            return pre_num
        else:
            pre_num+=1
    return False

t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    #直接取模！
    a=list(map(lambda y:int(y)%x,input().split()))
    if sum(a)%x!=0:
        print(n)
    else:
        off=min(prefix(a),prefix(a[::-1]))
        #print(prefix(a),prefix(a[::-1]))
        if not prefix(a) and (not prefix(a[::-1])):
            print(-1)
        else:
            print(n-off)




