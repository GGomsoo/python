# 도 개 걸 윷 모
# 배 0 등 1

for _ in range(3):
    old_game = list(map(int, input().split()))

    bae = 0
    deung = 0

    for i in range(4):
        if old_game[i] == 0:
            bae += 1
        if old_game[i] == 1:
            deung += 1

    if bae == 1 and deung == 3:
        print("A")
    if bae == 2 and deung == 2:
        print("B")
    if bae == 3 and deung == 1:
        print("C")
    if bae == 4 and deung == 0:
        print("D")
    if bae == 0 and deung == 4:
        print("E")