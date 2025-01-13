n,q=map(int,input().split())
c=[]

for i in range(q):
    a,b = map(int,input().split())
    if a>b:
        c.append([a,b])
    else:
        c.append([b,a])
d=set(str(i) for i in c)#集合查重
if len(d)==len(c):
    print("No")
else:
    print("Yes")

'''
答案有几句冗余
def has_mutual_likes( likes):
    like_set = set()
    for x, y in likes:
        if (y, x) in like_set:
            return "Yes"
        like_set.add((x, y))
    return "No"
找到一个就停止
n,q=map(int,input().split())
likes = [tuple(map(int, input().strip().split())) for _ in range(q)]
result = has_mutual_likes(likes)
print(result)'''