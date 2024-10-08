# 컴백홈
# 실버 I
## 출발: [R-1][0]
## 도착: [0][C-1]

def come_back_home(j, i, d):
    global ans
    visited[j][i] = 1

    if (j, i, d) == (0, C-1, K):
        ans += 1
        return
    
    dj = [-1, 0, 1, 0]
    di = [0, 1, 0, -1]

    for kk in range(4):
        nj = j + dj[kk]
        ni = i + di[kk]

        if 0 <= nj < R and 0 <= ni < C:
            if not visited[nj][ni] and camps[nj][ni] == ".":
                visited[nj][ni] = 1
                come_back_home(nj, ni, d+1)
                visited[nj][ni] = 0

R, C, K = map(int, input().split())
camps = [list(input()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]
ans = 0

come_back_home(R-1, 0, 1)

print(ans)