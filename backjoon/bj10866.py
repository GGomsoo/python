from collections import deque
import sys; input = sys.stdin.readline

N = int(input())
q = deque()

for _ in range(N):
    order = input().split()

    if "push_front" in order:
        q.appendleft(int(order[1]))
    
    if "push_back" in order:
        q.append(int(order[1]))

    if "pop_front" in order:
        if not q:
            print(-1)
        else:
            print(q.popleft())
    
    if "pop_back" in order:
        if not q:
            print(-1)
        else:
            print(q.pop())
    
    if "size" in order:
        print(len(q))
    
    if "empty" in order:
        if not q:
            print(1)
        else:
            print(0)
    
    if "front" in order:
        if not q:
            print(-1)
        else:
            print(q[0])
    
    if "back" in order:
        if not q:
            print(-1)
        else:
            print(q[-1])