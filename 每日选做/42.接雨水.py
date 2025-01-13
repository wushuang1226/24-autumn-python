height=[9,6,8,8,5,6,3]
n=len(height)
if n==1 or n==2:#特殊情况一定要有！
    print(0)
else:
    ans=0
    left=[0]*n
    right=[n-1]*n
    for i in range(1,n):
        if height[i]<height[left[i-1]]:
            left[i]=left[i-1]
        else:
            left[i] = i
        if height[i]>height[i-1]:
            for x in range(left[i-1],i+1):
                if height[i]>height[right[x]]:
                    right[x]=i
    for i in range(n):
        c=min(height[left[i]],height[right[i]])-height[i]
        if c>0:
            ans+=c
            print(i,ans)

    print(left)
    print(right)
    print(ans)

#法一 单调栈：到每一列后，按行接水
'''
stack=[]#相当于左边界
water = 0
for i in range(len(height)):
    while stack and height[i] > height[stack[-1]]:#高于左边界的是右边界
        top = stack.pop()#最低水位线
        if not stack:
            break
        distance = i - stack[-1] - 1
        bounded_height = min(height[i], height[stack[-1]]) - height[top]
        water += distance * bounded_height
    stack.append(i)
return water'''

#法二 双指针：按列接水，只要两侧有更高的就一定能接住
'''
ans = left = pre_max = suf_max = 0
right = len(height) - 1
while left < right:#双指针循环
    pre_max = max(pre_max, height[left])
    suf_max = max(suf_max, height[right])
    if pre_max < suf_max:#这列接住的水取决于两侧更低的一边
        ans += pre_max - height[left]
        left += 1
    else:
        ans += suf_max - height[right]
        right -= 1'''