h=int(input())
m=int(input())
#两天。。
h*=2
h-=m*0.5
#先刨去基础时间
a=[]
b=0
for i in range(m):
    a.append(list(map(float,input().split())))
#从高到低性价比复习（类似装糖果）
# 虽然AC了但这里的性价比应该乘上学分！！关注最终变量
#course.append(course[0] * course[1])  # 将性价比添加到每个课程的信息中
a.sort(reverse=True)#key=lambda x: -x[2]负数实现逆序

for i in range(m):
    #max_time_for_course = min(5 / course[0], total_time)
    if h-5/a[i][0]>0:
        h-=5/a[i][0]
        b+=5*a[i][1]
    else:
        b+=h*a[i][0]*a[i][1]
        break
print(f'{b:.1f}')
