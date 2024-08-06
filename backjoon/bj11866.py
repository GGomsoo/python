# N, K = map(int, input().split()) # N명의 사람, 제거할 순서 K

# q = list(i for i in range(1, N+1)) # 1번부터 N번까지의 사람 list
# ans = [] # 정답 list
# idx = 0 # 순서를 위한 변수


# while len(q) > 0: # 제거 명단에 사람이 없을 때 까지 while문 돌려
#     idx += (K-1) # 변수에 순서를 누적
#     if idx >= len(q): # 그 순서가 명단의 길이를 넘을 경우
#         idx %= len(q) # 명단의 길이로 나눈 나머지값을 변수로 설정
#     ans.append(q.pop(idx)) # 제거순서를 list에 추가
    
# print("<", end="")
# print(*ans, sep=", ", end="")
# print(">")

## 큐 활용해서 풀어보기 ( 구글서 힌트 얻음 )
from collections import deque

N, K = map(int, input().split())
q = deque(i for i in range(1, N+1))
ans = deque()

while len(q) > 0:
    for _ in range(K-1): # 제거 명단 전 순서까지 인원들을 뒤로 보낸다
        q.append(q.popleft())
    ans.append(q.popleft()) # 제거대상을 큐에 넣는다

print("<", end="")
print(*ans, sep=", ", end="")
print(">")