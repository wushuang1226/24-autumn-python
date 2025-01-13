n=input()
a=[0]*len(n)
b=[]
for j in range(len(n)-1):
    if n[j] == n[j + 1]:
        a[j]=1

m=int(input())
for i in range(m):
    l,r=map(int,input().split())
    b.append(str(sum(a[l-1:r-1])))#-1别忘了！！
    '''for j in range(l-1,r-1):
        if n[j]==n[j+1]:
            a+=1
    print(a)'''
print('\n'.join(b))

'''没懂这个答案的ans和12345……有啥区别呜呜
s = [str(i) for i in input()]
ans = [0]
num = 0
answer = []
for i in range(1, len(s)):
    if s[i]==s[i-1]:
        num += 1
    ans.append(num)
#哈哈哈我现在懂啦——这个是前缀和思想呐
for i in range(int(input())):
    l,r = map(int, input().split())
    answer.append(str(ans[r-1] - ans[l-1]))

print('\n'.join(answer))   '''