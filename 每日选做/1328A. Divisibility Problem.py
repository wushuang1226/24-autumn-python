t=int(input())
for i in range(t):
    n=0
    l=list(map(int,input().split()))
    a=l[0]
    b=l[1]
    if a%b==0:
        print(0)
    else:
        print(b-a%b)
#不可以逐步加1！！！要一步到位
