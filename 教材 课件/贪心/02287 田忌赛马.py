while True:
        try:
                n = int(input())
                a=list(map(int,input().split()))
                b=list(map(int,input().split()))
                a.sort()
                b.sort()
                c=0
                #最值入手
                #抉择用最快的还是最慢的比最快的和最慢的 选择“最值的”
                for i in range( n):
                    if a[-1]>b[-1]:
                        a.remove(a[-1])
                        b.remove(b[-1])
                        c+=200
                    elif a[-1]<b[-1]:
                        a.remove(a[0])
                        b.remove(b[-1])
                        c -= 200
                    elif a[-1]==b[-1]:
                        if a[0]>b[0]:
                            a.remove(a[0])
                            b.remove(b[0])
                            c += 200
                        elif a[0]<b[-1]:
                            a.remove(a[0])
                            b.remove(b[-1])
                            c -= 200
                print(c)
        except EOFError:
                break
