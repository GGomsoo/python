# 1분에 1~5 까지의 거리를 이동할 수 있다.
# 최대한 빨리 찾는 경우 몇 분 걸리는가?
dist = int(input()) # 성우의 현재위치와 민건이의 집까지의 거리

if dist % 5 == 0:
    print(dist // 5)
else:
    print(dist // 5 + 1)