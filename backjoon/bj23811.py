N = int(input()) # 셀의 크기 N

for i in range(5): # 가로 및 세로로 각각 5개의 셀로 구성
    for j in range(N): # 셀의 크기만큼 추가적인 for문
        if i % 2 == 0:
            print("@" * 5 * N)
        else:
            print("@" * N)