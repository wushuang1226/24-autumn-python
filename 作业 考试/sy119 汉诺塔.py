#递归：逆推思路
#n→n-1默写答案
#呜呜不会
def move(n,from_,to,mid):
    if n==0:
        return
    else:
        move(n-1,from_,mid,to)
        print(f"{from_}->{to}")#第n个
        move(n-1,mid,to,from_)

n=int(input())
print(2**n-1)#总次数……可以观察
move(n,'A',"C","B")
