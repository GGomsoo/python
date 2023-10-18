# 그룹나누기
# union, find 이용
def find_set(x):
    if parents[x] == x:
        return x
    else:
        return find_set(parents[x])


T = int(input())
for test1 in range(1, T + 1):
    N, M = map(int, input().split())
    parents = list(range(N + 1))  # make-set

    for i in range(M):
        s, g = map(int, input().split())

        # union
        parents[find_set(g)] = find_set(s)

    cnt = 0
    for i in range(1, N + 1):
        if parents[i] == i:
            cnt += 1

    print(f"#{test1} {cnt}")
