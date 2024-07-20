# DP
# 그리디

N = int(input()) # 배달 해야하는 설탕의 양

pack = 0 # 주머니 갯수
while(N >= 0):
    if N % 5 == 0: # 설탕의 양이 5의 배수?
        pack += N // 5 # 그 몫 만큼 주머니 갯수 추가
        print(pack)
        break
    N -= 3 # 3키로로 하나 포장
    pack += 1 # 주머니 갯수 추가
else: # 5로도 안되고, 3으로도 안되는건 -1 출력
    print(-1)