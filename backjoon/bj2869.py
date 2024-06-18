# 시간제한 0.25초 ( == 반복문으로 풀면 안된다 )
A, B, V = map(int, input().split())

if (V-B) % (A-B) == 0:
    print((V-B) // (A-B))
else:
    print(((V-B) // (A-B)) + 1)