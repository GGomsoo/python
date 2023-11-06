# 약수 구하기
# 브론즈 III
# 두 자연수 N, K 제공
# N의 약수들 중 K번째로 작은 수를 출력
# N의 약수의 개수가 K개보다 적어서 K번째 수가 없다면 0을 출력

# 두 자연수 N, K 제공
N, K = map(int, input().split())

# 약수들 넣을 리스트
factor = []

# 1부터 N까지
for i in range(1, N+1):
    # 나머지 0인 애들만 리스트에 추가
    if N % i == 0:
        factor.append(i)

# 약수 리스트 길이가 K보다 작다면
if len(factor) < K:
    # 0 출력
    print(0)
# 그게 아니라면
else:
    # K번째 숫자 출력
    # 인덱스는 0부터 시작이니까 K-1
    print(factor[K-1])