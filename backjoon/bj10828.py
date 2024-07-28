N = int(input())
my_stack = []

for _ in range(N):
    order = input().split()
    # push 명령인 경우
    if "push" in order:
        my_stack.append(int(order[1]))
    
    # pop 명령인 경우
    if "pop" in order:
        if len(my_stack) > 0:
            print(my_stack.pop())
        else:
            print(-1)
    
    # size 명령인 경우
    if "size" in order:
        print(len(my_stack))

    # empty 명령인 경우
    if "empty" in order:
        if len(my_stack) == 0:
            print(1)
        else:
            print(0)
    
    # top 명령인 경우
    if "top" in order:
        if len(my_stack) > 0:
            print(my_stack[-1])
        else:
            print(-1)

# 시간초과