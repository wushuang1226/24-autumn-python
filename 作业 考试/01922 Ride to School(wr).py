while True:
    n=int(input())
    if n==0:
        break

    b=[]
    for i in range(n):
        a=list(map(int,(input().split("	"))))
        b.append(a)

    v=0
    d=0
    t=0
    v0=[b[i][0] for i in range(n)]
    d0=[-b[i][0]*b[i][1]/3600 for i in range(n)]
    t0=[[x,0] for x in range(n)]

    while True:
        print(t,d,v)
        if all(d<=d0[i] for i in range(n)):
            break
        for i in range(n):
            if d - d0[i] >= 0 and v0[i] - v > 0:
                t0[i]=([i,(d - d0[i]) / (v0[i] - v)])
            else:
                t0[i]=[i,0]
        t = min([t0[i][1] for i in range(n) if t0[i][1]>0])
        d0 = [d0[i] + v0[i] * t for i in range(n)]
        d=d+v*t
        if d<4.5:
            v = max([v0[i] for i in range(n) if t0[i][1] == t])
        else:
            break


    t=(t-(d-4.5)/v)*3600
    print(int(t if t%1==0 else t//1+1))
