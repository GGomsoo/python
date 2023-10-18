# 일곱 난쟁이의 키 합 100 되는 조합 찾기


# 아홉 난쟁이의 키 입력
난쟁이들 = [int(input()) for _ in range(9)]
정답 = []
총합 = 0
for i in range(9):
    총합 += 난쟁이들[i]

원하는것 = 총합 - 100
빠져1 = 빠져2 = 0
for i in range(len(난쟁이들)-1):
    for j in range(i+1, len(난쟁이들)):
        if 난쟁이들[i]+난쟁이들[j] == 원하는것:
            빠져1 = 난쟁이들[i]
            빠져2 = 난쟁이들[j]

for i in range(len(난쟁이들)):
    if 난쟁이들[i] != 빠져1 and 난쟁이들[i] != 빠져2:
        정답.append(난쟁이들[i])
정답.sort()
for i in range(7):
    print(정답[i])
print()