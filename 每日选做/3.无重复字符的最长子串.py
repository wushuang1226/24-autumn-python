from collections import deque
s=input()
if len(s)==0:
    print(0)
else:
    q=deque(s[0])
    ans=[]
    for i in s:
        while q and i in q:
            q.popleft()
        q.append(i)
        #print(q)
        ans.append(len(q))
    print(max(ans))
'''记录每个字符最后出现的位置
k——当前无重复字符串start
            if c in c_dict and c_dict[c] > k:  # 字符c在字典中 且 上次出现的下标大于当前长度的起始下标
                k = c_dict[c]
            c_dict[c] = i
            res = max(res, i - k)'''
