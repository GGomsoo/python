카드개수N, 합M = map(int, input().split())
카드뭉치list = list(map(int, input().split()))
정답 = 0

for 첫째 in range(카드개수N):
    for 둘째 in range(첫째+1, 카드개수N):
        for 셋째 in range(둘째+1, 카드개수N):
            블랙잭 = 카드뭉치list[첫째] + 카드뭉치list[둘째] + 카드뭉치list[셋째]
            
            if 블랙잭 <= 합M:
                정답 = max(블랙잭, 정답)

print(정답)