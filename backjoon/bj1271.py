# 조교가 가진 돈 n
# 돈 받으러 온 생명의 수 m
# 돈을 똑같이 분배, 분배한 후 남는 돈

N, M = map(int, input().split())

print(N // M)
print(N % M)