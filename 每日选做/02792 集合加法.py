n=int(input())
for i in range(n):
    s=int(input())
    a=int(input())
    A=list(map(int,input().split()))
    b = int(input())
    B = list(map(int, input().split()))
    c=0
    for i in A:
        c+=B.count(s-i)
        #count函数比遍历b快了6倍
    print(c)
