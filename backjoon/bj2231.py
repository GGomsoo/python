# 어떤 자연수 N
N = int(input())

# 자연수 N에 대한 분해합
분해합 = 0

# 1부터 N까지
for i in range(1, N+1):
    
    # 숫자를 리스트화
    숫자 = list(map(int, str(i)))
    
    # 분해합 = i + 각 자리수의 합
    분해합 = sum(숫자) + i
    
    # 분해합과 N이 같으면
    # i는 N의 생성자
    if 분해합 == N:
        print(i)
        break
    
    # i랑 N이랑 같으면
    # 이 숫자는 생성자가 없다
    if i == N:
        print(0)