x=int(input())
while x!=1:
    if x%2==1:
        y=x*3+1
        print("%d*3+1=%d"%(x,y))
        x=y
    else:
        y=x/2
        print("%d/2=%d"%(x,y))
        x=y

