#辅助栈
l=[]
m=[]#辅助列表维护最小值！(空间换时间）
while True:
        try:
                a = input().split()
                if "push" in a:
                    top=int(a[1])
                    l.append(top)
                    if not m:
                        m.append(top)
                    else:
                        m.append(min(m[-1],top))
                if "pop" in a and len(l)!=0:
                    l.pop()
                    m.pop()
                    #mi=last_min拒绝缝缝补补！连着pop、两个就会出问题
                if "min" in a and len(l)!=0:
                    print(m[-1])#直接min(l)找最小值会超时
        except EOFError:
                break

#法二 懒删除
'''
import heapq
from collections import defaultdict

out = defaultdict(int)  # 字典，记每个元素被逻辑删除的次数
pigs_heap = []  # 最小堆，用于存储所有元素
pigs_stack = []  # 栈，用于处理pop操作

while True:
    try:
        s = input().strip()
    except EOFError:
        break

    if s == "pop":
        if pigs_stack:
            x = pigs_stack.pop()
            out[x] += 1  # 标记该元素已被逻辑删除
    elif s == "min":
        # 清除堆中已经被逻辑删除的最小元素
        while pigs_heap and out[pigs_heap[0]] > 0:
            out[pigs_heap[0]] -= 1
            heapq.heappop(pigs_heap)
        if pigs_heap:
            print(pigs_heap[0])
    else:
        y = int(s.split()[1])
        pigs_stack.append(y)
        heapq.heappush(pigs_heap, y)'''