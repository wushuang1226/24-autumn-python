#贪心的例题做过一次嘞 还记得吗？！
#bujidele......
#“理解性最优”
while True:
    n=int(input())
    if n==0:
        break
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.sort()
    b.sort()
    c=0
    while n>0:
        n-=1
        #一个一个来，还是从最快入手, 分类不重不漏！
        if a[-1]>b[-1]:
            '''a[0]>b[0] or '''
            a.pop(-1)
            b.pop(-1)
            c+=200
        elif a[-1]<b[-1]:
            a.pop(0)
            b.pop(-1)
            c-=200
        elif a[-1]==b[-1]:
            if a[0]>b[0]:
                a.pop(0)
                b.pop(0)
                c+=200
            elif a[0]<b[-1]:
                a.pop(0)
                b.pop(-1)
                c-=200
        '''elif a[-1]==b[-1]:#?
            a.pop(-1)
            b.pop(-1)'''

    print(c)
