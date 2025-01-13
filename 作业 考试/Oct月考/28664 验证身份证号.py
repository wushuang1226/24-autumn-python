#10min
#加一个检验长度


n =int(input())
b=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
e=['1','0','X','9','8','7','6','5','4','3','2']
for i in range(n):

    if len(s) != 18:
        print('NO')
        continue

    c=0
    m=input()
    a=[int(x) for x in m[:-1]]
    for j in range(17):
        c+=a[j]*b[j]
        d=c%11
    #print(e[d])自查
    if m[-1]==e[d]:
        print("YES")
    else:
        print("NO")
