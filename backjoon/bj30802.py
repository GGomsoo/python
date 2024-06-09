# 웰컴 키트
# 수학, 사칙연산

참가자 = int(input())
티셔츠사이즈 = list(map(int, input().split()))
티셔츠묶음, 펜묶음 = map(int, input().split())
정답1 = 0

for i in range(len(티셔츠사이즈)):
    if 티셔츠사이즈[i] % 티셔츠묶음 == 0:
        정답1 += int(티셔츠사이즈[i] / 티셔츠묶음)
    else:
        정답1 += int((티셔츠사이즈[i]/티셔츠묶음) + 1)
print(정답1)

정답2 = [int(참가자 / 펜묶음), int(참가자 % 펜묶음)]
print(*정답2)