#要让靠前的位数字尽可能小——遇到更小的，就把大的删掉
#生成的是不减数列
#添加一个末端维护
def num(n,k):
    stack=[]
    for i in n:
        while k and stack and stack[-1]>i:
            stack.pop()
            k-=1#计数器
        stack.append(i)
    while k:
        stack.pop()
        k-=1#如果有一样大的，末端减去
    stack=[str(___) for ___ in stack]
    return ''.join(stack)
t=int(input())
for _ in range(t):
    n,k=input().split()
    k=int(k)
    n=[int(__) for __ in n]
    print(num(n,k))