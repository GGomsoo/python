# 별 찍기 -7
# 브론즈 III

N = int(input())

for i in range(N):
    print(' ' * (N-i) + '*' * (i*2+1))

for i in range(N-2, -1, -1):
    print(' ' * (N-i) + '*' * (i*2+1))