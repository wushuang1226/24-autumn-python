while True:
        try:
                a = list(input())
                if a[::-1]==a:
                    print("YES")
                else:
                    print("NO")
        except EOFError:
                break
#队列 while len(num_deque) > 1:
#if num_deque.popleft() != num_deque.pop():