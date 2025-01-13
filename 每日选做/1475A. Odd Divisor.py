#这题看了答案
t=int(input())
for i in range(t):
    a=int(input())
    while True:
        if a%2==0:
            a=a/2
        else:
            if a>1:
                print("YES")
            else:
                print("NO")
            break
# 不断除以二，化偶数为奇数
