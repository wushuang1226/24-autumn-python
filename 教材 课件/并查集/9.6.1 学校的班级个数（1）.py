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

cl=set(find(x) for x in range(n))
print(len(cl))