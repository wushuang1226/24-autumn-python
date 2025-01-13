ra,ca=map(int,input().split())
A=[list(map(int,input().split())) for i in range(ra)]
rb,cb=map(int,input().split())
B=[list(map(int,input().split())) for i in range(rb)]
rc,cc=map(int,input().split())
C=[list(map(int,input().split())) for i in range(rc)]

#列表默认+*为加长
D=[[0 for x in range(cc)] for y in range(rc)]
if ca!=rb or ra!=rc or cb!=cc:
    print("Error!")
else:
    for x in range(ca):
        for i in range(ra):
            for j in range(cb):
                D[i][j] += A[i][x] * B[x][j]
    #            D[i][j] += C[i][j]不用再循环一遍
    for i in range(rc):
        for j in range(cc-1):
            print(str(C[i][j] + D[i][j]),end=" ")
            #join函数代替end或者用print（*list）
        print(str(C[i][cc-1]+D[i][cc-1]))




