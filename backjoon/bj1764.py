import sys

N, M = map(int, input().split())

n_l_p = set()
n_s_p = set()
ans_people = []

for _ in range(N):
    n_l_p.add(sys.stdin.readline().rstrip())

for _ in range(M):
    n_s_p.add(sys.stdin.readline().rstrip())

ans_people = sorted((n_l_p) & (n_s_p)) # 정답

# 아래 코드는 오답 코드
# 듣도(보도) 못한 사람이 보도(듣도) 못한 사람 명단에도 있으면
# 정답 리스트에 append
# 해당 리스트의 len과 for문을 이용하여 인원들을 출력하도록 코드 작성
# 테스트 케이스는 정답이었지만, 문제 제출엔 오답처리

# if len(n_l_p) > len(n_s_p):
#     for people in n_s_p:
#         if people in n_l_p:
#             ans_people.append(people)

# else:
#     for people in n_l_p:
#         if people in n_s_p:
#             ans_people.append(people)

print(len(ans_people))

for ans in ans_people:
    print(ans)