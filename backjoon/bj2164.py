# N장의 카드가 있다. 카드는 1부터 N까지의 번호로 이루어짐
# 1번 카드가 맨 위에 있다. => list의 맨 오른쪽에 있다.
# 카드가 1장 남을 때 까지 다음 동작을 반복
# 맨 위에 카드를 뺀다 (pop) -> 그 다음 맨 위 카드를 맨 아래로 보낸다 (appendleft)

from collections import deque
import sys

N = int(sys.stdin.readline())

my_queue = deque()

for i in range(1, N+1):
    my_queue.appendleft(i)

while(len(my_queue) > 1):
    my_queue.pop()
    my_queue.appendleft(my_queue.pop())

print(*my_queue)