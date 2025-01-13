N = L = 0
used = []
length = []

def Dfs(R, M):
    if R == 0 and M == 0:
        return True
    if M == 0:
        M = L

    for i in range(N):
        if used[i] == False and length[i] <= M:
            if i > 0:
                if used[i - 1] == False and length[i] == length[i - 1]:
                    continue  # 不要在同一个位置多次尝试相同长度的木棒，剪枝1

            used[i] = True#True表示用过的“旧”标记
            #####
            if (Dfs(R - 1, M - length[i])):
                return True
            #####继续往下能否走通
            else:
                used[i] = False

                # 不能仅仅通过替换最后一根木棒来达到目的，剪枝3
                # 替换第一个根棍子是没有用的，因为就算现在不用，也总会用到这根木棍，剪枝2
                if length[i] == M or M == L:
                    return False

    return False


while True:
    N = int(input())
    if N == 0:
        break

    length = [int(x) for x in input().split()]
    length.sort(reverse=True)  # 排序是为了从长到短拿木棒进行尝试

    totalLen = sum(length)

    for L in range(length[0], totalLen // 2 + 1):
        if totalLen % L:
            continue  # 不是木棒长度和的因子的长度，直接否定

        used = [False] * 65
        if Dfs(N, L):
            print(L)
            break

    else:
        print(totalLen)