# ACM 호텔
# 브론즈 III

# test case 갯수
T = int(input())
for _ in range(T):

    # 순서대로 층수, 넓이, 번호표
    H, W, N = map(int, input().split())

    # 층수 = 손님의 순서를 전체 건물높이로 나눈 나머지 값
    floor_num = N % H

    # 방 번호 = 손님의 순서를 전체 층수로 나눈 몫 + 1
    room_num = N // H + 1

    # 만약 손님의 순서랑 건물높이가 같은 경우
    if N % H == 0:

        # 손님의 층수 = 건물의 높이
        floor_num = H

        # 방 번호 = 손님의 순서를 전체 층수로 나눈 값
        room_num = N // H

    # 층수 * 100 + 방번호 = 1001 이런식으로 방 호수를 결과값으로 얻음
    print(floor_num * 100 + room_num)