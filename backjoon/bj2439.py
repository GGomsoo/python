# 별찍기 -2
# 브론즈 IV

N = int(input())

for i in range(1, N+1):
    print(' ' *(N-i) + '*' * i)
print()