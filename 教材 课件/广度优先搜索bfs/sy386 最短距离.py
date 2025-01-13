n,m,s,t=map(int,input().split())
a=[list(map(int,input().split()))for i in range(m)]
import heapq
###Dijkstra：超级大乱炖
#bfs，dp，greedy heapq
def bfs(s,t):
    #无序路径！
    graph=[[] for _ in range(n)]
    q = [(0,s)]
    inq = set()
    inq.add((0,s))#其实这个不需要d
    for u, v, w in a:
        graph[u].append((v,w))
        graph[v].append((u,w))
        #类似字典的映射
    dp=[float("inf")]*n
    dp[s]=0
    while q:
        d,p=heapq.heappop(q)
        if p==t:
            return d
        for np,w in graph[p]:
            if  (d+w,np) not in inq and d+w<dp[np]:
                dp[np]=d+w
                heapq.heappush(q, (d+w, np))
                inq.add((d+w, np))
    return -1

print(bfs(s,t))


