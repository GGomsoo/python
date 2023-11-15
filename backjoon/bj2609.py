# 최대공약수 최소공배수
# 브론즈 I

# 숫자 2개 입력
A, B = map(int, input().split())

# 약수 넣을 리스트들
A_lst = []
B_lst = []

# 숫자 A에 대한 약수 구하기
for i in range(1, A+1):
    if A % i == 0:
        A_lst.append(i)

# 숫자 B에 대한 약수 구하기
for j in range(1, B+1):
    if B % j == 0:
        B_lst.append(j)

# 공약수 리스트 구하기
# 중복 없애고 and로 묶어버림
ans_lst = set(A_lst) & set(B_lst)

# 영어 쓸라다가 너무 길어서 걍 한글써버림
최대공약수 = max(ans_lst)
최소공배수 = 최대공약수 * (A // 최대공약수) * (B // 최대공약수)

print(최대공약수)
print(최소공배수)