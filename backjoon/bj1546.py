# 평균
# 브론즈 I

# 점수조작
# 자기 점수 중 최댓값 M 을 고름.

# 시험 본 과목의 갯수
N = int(input())
# 그 과목에 대한 점수
scores = list(map(int, input().split()))

# 자기 점수 중 최댓값
M = max(scores)
# 새로운 점수를 넣을 리스트
ans = []

for score in scores:
    # ans 리스트에 얻은 점수를 최댓값으로 나누고 
    # 그걸 * 100한 점수를 추가
    ans.append(score / M * 100)

final_ans = 0
# 과목 갯수에 대해
for i in range(N):
    # 최종 점수에 아까 점수조작한 리스트의 점수들을 누적
    final_ans += ans[i]

# 전체 점수 / 과목 갯수
print(final_ans / N)