#逐一遍历是非常不科学的！！
#避免重复项！！——没有必要储存完整的字符串

sequence = ""
s = 0
ss = 0
sums = []

#前缀合思想与分段思想
for j in range(1, 33000):
    sequence += str(j)
    s += len(str(j))#每段长度
    ss += s  #总长度
    sums.append(ss)
#print(ss)
test_cases = int(input())
for _ in range(test_cases):
    x = int(input())

    if x == 1:
        print(1)
    else:
        # 在累加和列表中查找第一个大于等于 x 的元素
        for i in range(len(sums)):
            if x <= sums[i]:
                print(sums[:i+1])
                # 计算偏移量并从序列中输出数字
                offset = x - sums[i-1] - 1
                print(sequence[offset])
                break