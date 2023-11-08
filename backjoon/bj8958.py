# OX 퀴즈
# 브론즈 II
# IM 문제였음

N = int(input())

for _ in range(N):
    # 답지 입력
    answer = input()

    # 최종 점수
    total_point = 0
    # 문제 맞췄을 때 마다 더해질 점수
    point = 0

    # 답지 검사하는데
    for i in answer:
        # 맞췄으면
        if i == 'O':
            # 점수 1씩 누적
            # 연속으로 맞추면 point에 1씩 누적되면서
            point += 1
            # 최종 점수에 차근차근 누적
            total_point += point
        # 틀리면 0점
        else:
            point = 0

    print(total_point)