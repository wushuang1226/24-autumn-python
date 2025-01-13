import math

while True:
    n = int(input())
    all_time=[]
    if n == 0:
        break

    #max_time = float("inf")？？
    for _ in range(n):
        speed, time = map(int, input().split())
        if time < 0:
            continue
        arrival_time = math.ceil((4.5 / speed) * 3600 + time)
        all_time.append(arrival_time)
        min_time = min(all_time)
#emmmm实在是把问题想得太复杂了嘞 没有抓住本质
    #就是跟着第一个到的人到达……
#一定先努力化简翻译题！！！
    print(min_time)