#学习定义函数
#数据量很小，只有10，放心遍历
"""
答案：{字典}的用法！！！！！
def has_three_way_likes(n, q, likes):
    like_dict = {}
    for x, y in likes:
        if x not in like_dict:
            like_dict[x] = set()
        like_dict[x].add(y)

    for a in like_dict:
        for b in like_dict[a]:
            if b in like_dict:
                for c in like_dict[b]:
                    if c in like_dict and a in like_dict[c]:
                        return "Yes"
    return "No"
"""
def has_triple_likes(likes):
    for i in likes:
        for j in likes:
            for k in likes:
                if i[1] == j[0] and j[1] == k[0] and k[1] == i[0]:
                    return "Yes"
    return "No"

n,q=map(int,input().split())
likes = [tuple(map(int, input().strip().split())) for _ in range(q)]
result = has_triple_likes(likes)
print(result)