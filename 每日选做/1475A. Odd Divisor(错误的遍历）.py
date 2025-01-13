t=int(input())
b=0
for i in range(t):
    a=int(input())
    for j in range(3,10**14,2):
        if a%j==0:
            print('YES')
            b=1
            break
    if b==0:
        print("NO")
    b=0
        
