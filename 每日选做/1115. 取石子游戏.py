#完全没懂 但是给了提示？
#也可以直接递归!保存函数数据即可 for i in range(1,a//b+1):if can_win(a,b-a*i)
def stone(a,b,c):
    #print(a,b,c)
    if a//b>=2 or a==b:#取等特殊分析！
        return c
    else:
        a,b=b,a-b
        return stone(a,b,c+1)
while True:
    a,b=map(int,input().split())
    if a==b==0:
        break
    if a<b:
        a,b=b,a
    if stone(a,b,1)%2==1:
                print("win")
    else:
                print("lose")

