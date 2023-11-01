# 최댓값
# 브론즈 III
# 9 X 9 격자판

N = 9
# 격자판 정보
arr = [list(map(int, input().split())) for _ in range(N)]

# 최댓값의 좌표 구하는 함수
def maxij():
    for i in range(N):
        for j in range(N):
            if max_num == arr[i][j]:
                return i, j

# 최댓값들
max_num = 0
max_i = 0
max_j = 0

# 격자판에 대하여
for i in range(N):
    for j in range(N):
        # 최댓값을 계속 찾아보자
        max_num = max(max_num, arr[i][j])

# 구한 최댓값을 이용해서 좌표 구하기
max_i, max_j = maxij()

print(max_num)
# 위에서 구한 좌표는 인덱스 값이기 때문에 +1씩 해준다.
print(max_i+1, max_j+1)