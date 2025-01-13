#四舍五入可能出问题
#delta
import math
n =int(input())
for i in range(n):
    a,b,c=list(map(float,input().split()))
    d=b * b - 4 * a * c
    if d>0:
        x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
        x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
        print('x1=%.5f;x2=%.5f'%(x1,x2))
    if d==0:
        #可简化 或者由于误差必须简化
        x=-b/(2*a)
        if x==0:
        #否则有-0
            print('x1=x2=%.5f'%(0))
        else:
            print('x1=x2=%.5f'%(x))
    if d<0:
        #实部虚部分开
        y1=math.sqrt(-b * b + 4 * a * c) / (2 * a)
        y2=math.sqrt(-b * b + 4 * a * c) / (2 * a)
        real=-b/(2*a)
        print('x1=%.5f+%.5fi;x2=%.5f+%.5fi'%(real,y1,real,y2))






