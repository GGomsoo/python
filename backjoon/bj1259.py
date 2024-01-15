while True:
    N = input()
    M = len(N)
    
    if int(N) == 0:
        break
    
    # 홀수
    if M // 2 != 0:
        for i in range(M//2 + 1):
            if N[i] == N[M-i-1]:
                print('yes')
            else:
                print('no')
                break