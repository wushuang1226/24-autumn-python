n=int(input())
A={a**3:a for a in range(2,n+1)}
B=[]
#a(3,n+1) b(2,a)
for b in range(2,n+1):
        for c in range(b,n+1):
            for d in range(c,n+1):
                if b**3+c**3+d**3 >n**3:
                    break
                if b**3+c**3+d**3 in A:
                    #字典默认在键中查找
                    B.append((A[b**3+c**3+d**3],b,c,d))
B.sort()
for i in range(len(B)):
    print("Cube = %d, Triple = (%d,%d,%d)"%(B[i][0],B[i][1],B[i][2],B[i][3]))
