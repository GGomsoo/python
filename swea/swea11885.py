import sys; sys.stdin=open("swea11885_input.txt")

tc = int(input())

for i in range(1, tc+1):
    N, M = map(int, input().split()) # 화덕의 크기 N, 피자 개수 M
    cheese = [0] + list(map(int, input().split())) # 피자에 뿌린 치즈의 양
    idx = list(range(1, N+1)) # 동시에 구울 수 있는 피자의 번호들 [1, 2, 3]

    while len(idx) > 1:
        num = idx.pop(0) # 맨 앞 자리에 있는 피자 번호
        cheese[num] //= 2 # 한바퀴 돌 때, 녹지 않은 치즈의 양은 반으로 줄어든다

        if cheese[num] != 0: # 치즈가 덜 녹았다면
            idx.append(num) # 다시 넣는다
        
        else: # 치즈가 다 녹았다면
            if N < M:
                N += 1
                idx.append(N)
    
    print(f"#{i} {idx[0]}")