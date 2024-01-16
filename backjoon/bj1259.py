while True:
    N = input()
    M = len(N)
    
    if int(N) == 0:
        break
    
    # 입력값의 길이가 홀수
    if M // 2 != 0:
        flag = 1
        for i in range(M//2 + 1):
            if N[i] != N[M-i-1]:
                flag = 0
                print('no')
                break
        
        if flag:
            print('yes')

    # 입력값의 길이가 짝수
    if M // 2 == 0:
        flag = 1
        for i in range(M//2):
            if N[i] != N[M-1-i]:
                flag = 0
                print('no')
                break
        if flag:
            print('yes')