def find(i):
    if parent[i]==i:
        return i
    else:
        return find(parent[i])

def union(i,j):
    pi=find(i)
    pj=find(j)
    parent[pi]=pj#i并入j

n,m=map(int,input().split())
parent=[i for i in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    union(a-1,b-1)

k=int(input())
for i in range(k):
    a,b=map(int,input().split())
    if find(a-1)==find(b-1):#-1-1-1-1-1
        print("Yes")
    else:
        print("No")