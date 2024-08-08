N, M = map(int, input().split())

chess = [input() for _ in range(N)] # 내게 주어진 체스판
ans = 0

for i in range(N-7): # 8 * 8 체스판으로 잘라낸 후 확인
    for j in range(M-7): # 체스판의 시작점 for문
        white_recover = 0 # 흰색으로 새로 색칠한 갯수
        black_recover = 0 # 검정색으로 새로 색칠한 갯수

        for a in range(i, i+8): # 잘라낸 부분의 시작점에서 8*8 만큼 for문 실행
            for b in range(j, j+8):
                if (a+b) % 2 == 0: # 짝수칸 ( == 체스판의 [0][0]과 같은 색깔 )
                    if chess[a][b] != "W":
                        white_recover += 1
                    else:
                        black_recover += 1
                else: # 홀수칸
                    if chess[a][b] != "B":
                        white_recover += 1
                    else:
                        black_recover += 1

        ans = min(white_recover, black_recover)

print(ans)