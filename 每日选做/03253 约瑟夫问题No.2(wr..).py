#implementation
def f(a,s,m):
    if len(a)==0:
        return
    else:#while len(a)>0循环！
        e=(s+m)%len(a)
        #print(e,a)
        ans.append(str(a[e-1]))
        a.pop(e-1)
        if e==1:
            f(a,len(a),m)
        else:
            f(a,e-1,m)

while True:
        try:
                n,p,m=map(int,input().split())
                if n==p==m==0:
                    break
                a = [i for i in range(1, n + 1)]
                s = p - 1
                ans=[]
                f(a,s,m)
                print(','.join(ans))
        except EOFError:
                break

