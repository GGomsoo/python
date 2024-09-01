from collections import deque

N, M = map(int, input().split()) # 큐의 크기 N, 뽑아내려는 수의 개수 M
arr = list(map(int, input().split())) # 뽑아내려는 수의 위치가 순서대로 주어짐
q = deque(range(1, N+1)) # 위치는 1보다 크거나 같고, N보다 작거나 같다

left = right = 0

for pick in arr: # 뽑아내려는 수 중에서

    while True:
        if q[0] == pick: # q의 첫번째 원소가 뽑아내려는 수와 같다면
            q.popleft() # 뽑아낸다
            break
        else:
            if q.index(pick) > len(q) // 2: # 찾는 숫자의 위치가 q의 길이의 절반보다 크다면
                q.appendleft(q.pop()) # 오른쪽으로 이동
                right += 1
            else: # 반대의 경우에는
                q.append(q.popleft()) # 왼쪽으로 이동
                left += 1

ans = left + right
print(ans)