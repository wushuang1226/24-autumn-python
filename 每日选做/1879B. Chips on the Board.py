#????这个看起来就好难啊
#翻译：行or列铺满，另一维度取最小
t=int(input())

for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    print(min(sum(a)+n*min(b),sum(b)+n*min(a)))
