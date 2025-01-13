while True:
    n=list(map(int,input().split()))
    if n==[0,0,0,0,0,0]:
        break
    a=0
    a+=n[5]+n[4]+n[3]+n[2]//4
    n[0]-=n[4]*11
    b = n[3] * 5
    while b>0:
        while n[1]>0 and b>0:
            n[1]-=1
            b-=1
        b=b*4
        n[0]-=1

    if n[2]%4!=0:
        a+=1
        b=n[2] % 4*5
        while n[1] > 0 and b > 0:
                n[1] -= 1
                b -= 1
        b = b*4+11
        while b>0:
            n[0] -= 1
            b-=1

    while n[1]>0:
        a+=n[1]//9+1
        b=36-4*n[1]%9
        while n[0] > 0 and b > 0:
            n[0] -= 1
            b -= 1

    while n[0]>0:
        a += n[0] // 36 + 1
    print(a)

