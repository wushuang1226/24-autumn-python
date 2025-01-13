n=int(input())
a=[]
b=[]
a.append(list(input()))
l= len(a[-1])
for i in range(n-1):
    a.append(list(input()))
    l=min(l,len(a[-1]))
for i in range(l):
    if all(j[i]==a[0][i] for j in a):#all加循环条件
        b.append(a[0][i])
    else:
        break

print(''.join(b))
'''def common_prefix(strs):
    if not strs:
        return ""

    # Start with the first string as the prefix
    prefix = strs[0]

    for s in strs[1:]:
        # Update the prefix by comparing it with each string
        while s[:len(prefix)] != prefix and prefix:前缀不是空会返回True
            prefix = prefix[:-1]删除末尾
        if not prefix:
            break

    return prefix'''