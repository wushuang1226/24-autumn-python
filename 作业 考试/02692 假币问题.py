#计算机思维！只有二十四种可能！
#brute fooooorce
"""意思没问题 就是好啰嗦。。
left, right, res = item.split()
left_total = sum(coins[i] for i in left)
coins = {coin: 0 for coin in 'ABCDEFGHIJKL'}直接给字母重量"""

dic={'A':0,"B":1,'C':2,"D":3,"E":4,"F":5,"G":6,'H':7,'I':8,'J':9,'K':10,'L':11}
dic2={x:y for y,x in dic.items()}#对调
dic3={1:"heavy",-1:"light"}

def coin(i, t):
    a[i] = t
    for j in range(3):
        ll = 0
        rr = 0
        for l in left[j]:
            ll += a[l]
        for r in right[j]:
            rr += a[r]
        # print(ll,rr)
        if outcome[j] == 'even':
            if ll != rr:
                return False
        if outcome[j] == 'up':
            if ll <= rr:
                return False
        if outcome[j] == 'down':
            if ll >= rr:
                return False
    return True

n=int(input())
for __ in range(n):
    left=[[] for i in range(3)]
    right=[[] for i in range(3)]
    outcome=[]
    for i in range(3):
        b=input()
        for j in range(4):
            left[i].append(dic[b[j]])
        for j in range(5,9):
            right[i].append(dic[b[j]])
        outcome.append(b.split()[-1])
    #print(left,right,outcome)
    a=[0]*12
    haha=1
    for i in range(12):
        for t in [-1,1]:
            if coin(i,t) and haha==1:
                c=dic2[i]
                d=dic3[t]
                print(f"{c} is the counterfeit coin and it is {d}.")
                haha=0
            else:
                a[i]=0#还原