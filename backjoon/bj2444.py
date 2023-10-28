# 별 찍기 -7
# 브론즈 III

# 별찍기인데 좀 더 생각하고 풀어야 할 문제

N = int(input())

for i in range(N*2):
    if i < N:
        print(' ' * (N-i) + '*' * (i*2+1) + ' ' * (N-i))
    else:
        print(' ' * (i-N) + '*' * (N*2+1-i) + ' ' * (i-N))
print()