# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

## 1회차 시도 - 시간초과
## 2회차 기존 input을 빠른 입력으로 변경 후 통과

import sys
from collections import deque

N = int(sys.stdin.readline())
my_queue = deque([])

for _ in range(N):
    order = sys.stdin.readline().split()

    if "push" in order:
        my_queue.append(order[1])

    if "pop" in order:
        if len(my_queue) != 0:
            print(my_queue.popleft())
        else:
            print(-1)

    if "size" in order:
        print(len(my_queue))

    if "empty" in order:
        if len(my_queue) == 0:
            print(1)
        else:
            print(0)

    if "front" in order:
        if len(my_queue) != 0:
            print(my_queue[0])
        else:
            print(-1)
    
    if "back" in order:
        if len(my_queue) != 0:
            print(my_queue[-1])
        else:
            print(-1)