# 킹, 퀸, 룩, 비숍, 나이트, 폰
# 브론즈 V

# 체스는 총 16피스
# 킹1개, 퀸1개, 룩2개, 비숍2개, 나이트2개, 폰8개
chess_unit = [1, 1, 2, 2, 2, 8]

# 내가 주운 체스판
find_chess = list(map(int, input().split()))

# 체스판 말 갯수 만큼 for문 진행
for i in range(len(chess_unit)):
    # 체스판 기본 셋팅 - 내가 주운 체스판, 띄어쓰기 해서 결과값 나란히 붙여서 출력
    print(chess_unit[i] - find_chess[i], end=' ')