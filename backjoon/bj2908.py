# 상수
# 브론즈 II
# 입력받은 숫자 뒤집어서 최대값 구하기

# 문자열로 두 수 입력받음
A, B = input().split()
# 자리수는 총 세자리수 
N = 3
# 거꾸로 읽은 숫자 A, B
A_reverse = ''
B_reverse = ''

# 뒤에서부터 앞으로 for문 진행
for i in range(N-1, -1, -1):
    # 거꾸로 읽은 숫자에 하나씩 넣기
    A_reverse += A[i]
    B_reverse += B[i]
# 둘 중 큰 수 비교
print(max(A_reverse, B_reverse))