q=int(input())
for i in range(q):
    k=0
    n=int(input())
    #直觉上的翻译是正确的 总和满足即可
    #过滤器
    a= filter(lambda x : x <= 2048,  map(int, input().split()) )
    '''for i in a:
        if i==2048:
            k=1
            break
        if i >2048:
            a.remove(i)
            #不要边修改边遍历！！！！！'''
    if sum(a)>=2048:
        print("YES")
    else:
        print("NO")

