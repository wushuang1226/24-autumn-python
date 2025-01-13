#emmmmz作弊一下?
nums=[5,7,7,8,8,10]
target=10
ans1=-1
ans2=-1
import bisect
if bisect.bisect_left(nums,target)<len(nums) and nums[bisect.bisect_left(nums,target)]==target:
    ans1=bisect.bisect_left(nums,target)
if bisect.bisect_right(nums,target)-1>=0 and nums[bisect.bisect_right(nums,target)-1]==target:
    ans2=bisect.bisect_right(nums,target)-1
print([ans1,ans2])
