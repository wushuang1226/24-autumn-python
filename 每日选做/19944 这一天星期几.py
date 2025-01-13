n=int(input())
b=['Sunday', 'Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday', 'Saturday']
#左开右闭!!
for i in range(n):
    a=input()
    c=int(a[0:2])
    y=int(a[2:4])
    m=int(a[4:6])
    if m<3 and y!=0:
        m+=12
        #上一年
        y-=1
    #整百年的特殊情况！
    if m<3 and y==0:
        m+=12
        c-=1
        y=99
    d=int(a[6:8])
    v=y+y//4+c//4-2*c+26*(m+1)//10+d-1
    print(b[v%7])
    
