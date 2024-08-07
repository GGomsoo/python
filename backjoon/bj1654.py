# 영식이가 자체적으로 갖고있는 길이 제각각의 랜선 K
# 성원이는 모든 랜선을 같은 길이의 N개로 만들고 싶어한다
# 이분 탐색 사용하기
import sys
input = sys.stdin.readline

K, N = map(int, input().split()) # 갖고있는 랜선 K, 필요한 갯수 N

lines = [] # 랜선 담을 봉투

for _ in range(K):
    lines.append(int(input())) # 랜선 넣고

front, end = 1, max(lines) # 최소값 1, 최대값은 봉투에 있는 랜선 중 가장 길이가 큰 친구

while front <= end: # 이분 탐색 시작
    mid = (front + end) // 2 # 중간값 설정
    ans = 0 # 필요한 갯수보다 많이 만드나? 적게 만드나? 기준점

    for i in lines:
        ans += i // mid # 봉투에 담긴 랜선들을 자르고, 잘린 갯수를 ans에 더한다
    
    if ans >= N: # 자른 갯수가 처음에 필요한 갯수보다 많거나 같은 경우
        front = mid + 1 # 랜선이 짧다
    else: # 적은 경우
        end = mid - 1 # 랜선이 길다

print(end)