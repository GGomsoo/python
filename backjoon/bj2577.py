# 숫자의 개수
# 브론즈 II

# 숫자 3개 입력
A = int(input())
B = int(input())
C = int(input())

# 숫자 3개 다 곱한 값
# 문자열 처리
D = str(A * B * C)

# 몇개 썼는지 확인할 0부터 9까지의 리스트
arr = [0] * 10

# 숫자 3개 다 곱한값의 길이만큼
for i in range(len(D)):
    # 1부터 10까지 중에
    for j in range(10):
        # j랑 D의 인덱스 호출값이랑 같으면
        if j == int(D[i]):
            # arr의 j번째에 1씩 누적
            # 그 숫자를 몇 번 썼는지 확인용
            arr[j] += 1

# 결과출력
for i in arr:
    print(i)