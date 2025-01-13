#不可以枚举法遍历！！！一步到位！
#抄答案时间……
    #abcdef省去列表
    #从大到小填，填满一个再填下一个
    #直接作差 算剩余空间
import math
rest = [0, 5, 3, 1]

while True:
    a, b, c, d, e, f = map(int, input().split())
    if a + b + c + d + e + f == 0:
        break
    boxes = d + e + f  # 装4*4, 5*5, 6*6
    boxes += math.ceil(c / 4)  # 填3*3
    spaceforb = 5 * d + rest[c % 4]  # 能和4*4 3*3 一起放的2*2
    if b > spaceforb:
        boxes += math.ceil((b - spaceforb) / 9)
    spacefora = boxes * 36 - (36 * f + 25 * e + 16 * d + 9 * c + 4 * b)  # 和其他箱子一起的填的1*1

    if a > spacefora:
        boxes += math.ceil((a - spacefora) / 36)
    print(boxes)

