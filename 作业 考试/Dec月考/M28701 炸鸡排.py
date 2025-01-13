#~ dian chi greedy贪心很简洁的┭┮﹏┭┮
n,k=map(int,input().split())
a=list(map(int,input().split()))
#理想为平均值，除非最长的更长只能放那一直炸
a.sort()
t=sum(a)
for i in a[::-1]:
    if i>t/k:
        k-=1
        t-=i
    else:
        print("%.3f"%(t/k))
        break