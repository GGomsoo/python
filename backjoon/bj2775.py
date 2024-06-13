T = int(input())

for _ in range(T):
    K = int(input()) # 층
    N = int(input()) # 호실
    Z_Floor = [x for x in range(1, N+1)] # 0층에 사는 인원들
    # print(Z_Floor) # 0층 사는 사람들 인원 확인

    for i in range(K):
        for j in range(1, N): # 호실에 대한 값을 리스트의 인덱스로 활용
            Z_Floor[j] += Z_Floor[j-1] # 기존 0층 인원에 값을 누적
        # print(Z_Floor)
    print(Z_Floor[-1]) # 마지막 호실 사람 인원 확인