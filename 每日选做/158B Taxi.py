#装箱问题的简化版本
import math
n=int(input())
a=list(map(int,input().split()))
c=0
c+=a.count(4)+a.count(3)+math.ceil(a.count(2)/2)
b=a.count(3)+(a.count(2)%2)*2
if b<a.count(1):
    c+=math.ceil((a.count(1)-b)/4)
print( c)