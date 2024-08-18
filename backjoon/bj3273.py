import sys
input = sys.stdin.readline

N = int(input()) # 수열의 크기
lst = sorted(map(int, input().split())) # 수열에 포함되는 수
X = int(input()) # 자연수 X
ans = 0

# 두 포인터 알고리즘
s, e = 0, N-1 # 시작점, 끝점 설정
while s < e:
    ssum = lst[s] + lst[e] # 임의의 합 == 수열의 시작 숫자 + 수열의 끝 숫자

    if ssum == X: # 임의의 합이 자연수와 같으면
        ans += 1 # 정답 += 1
        s += 1 # 수열의 시작점 우측으로 한 칸 이동
    
    if ssum < X: # 작아도 한 칸 이동
        s += 1
    
    if ssum > X: # 크면 끝점을 왼쪽으로 한 칸 이동
        e -= 1

print(ans)