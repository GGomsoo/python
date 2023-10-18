# swea 2105 - 모의 sw 역량테스트 - 디저트 카페
# 대각선으로 이동한다
# 갔던데는 다시 안간다
# 개어렵다 *****
def 함수(n, si, sj, v):
    global ans
    # 절반 가보고 아니다 싶어서 가지 치기
    if n == 2 and ans >= len(v) * 2:
        return

    # 가지 치기
    if n > 3:
        return

    # 재귀 종료 조건 = 시작 지점으로 돌아왔을 때
    if n == 3 and (i, j) == (si, sj):
        ans = max(ans, len(v))
        return

    # 반복문 ( 방향 전환 ) - 직진 아니면 방향 전환
    for k in range(n, n+2):
        ni = si+di[k]
        nj = sj+dj[k]
        # 방향 전환하는데 그게 범위안에 있다면?
        if 0 <= ni < N and 0 <= nj < N:
            # 들른곳 아니라면?
            if desserts[ni][nj] not in v:
                # 방문체크 느낌인듯..?
                v.append(desserts[ni][nj])
                함수(k, ni, nj, v)
                v.pop()


T = int(input())
for test1 in range(1, T+1):
    N = int(input())
    desserts = [list(map(int, input().split())) for _ in range(N)]

    # 방향전환용 리스트인데 왜 5개인지도 이해 X
    di = [1, 1, -1, -1, 1]
    dj = [-1, 1, 1, -1, -1]

    ans = -1

    # for 문 범위설정 왜 이렇게?
    for i in range(N-2):
        for j in range(1, N-1):
            함수(0, i, j, [])

    print(f"#{test1} {ans}")
