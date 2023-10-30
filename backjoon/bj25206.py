# 너의 평점은
# 실버 V
# 전공평점 = 전공과목별 (학점 x 과목평점) 의 합

# 실패, 원인을 잘 모르겠다.

# 과목의 수
N = 20

# 딕셔너리 사용하는 풀이 있던데 활용 X
# g = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]
# r = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']

# 전공과목별 점수
get_grade = 0

# 학점 총합
total_grade = 0

for _ in range(N):
    # 과목, 학점, 등급 입력
    subject, grade, rating = input().split()
    
    # 획득 등급? 별 학점 계산
    if rating == 'A+':
        get_grade += float(grade) * 4.5
        total_grade += float(grade)
        
    if rating == 'A0':
        get_grade += float(grade) * 4.0
        total_grade += float(grade)
        
    if rating == 'B+':
        get_grade += float(grade) * 3.5
        total_grade += float(grade)
        
    if rating == 'B0':
        get_grade += float(grade) * 3.0
        total_grade += float(grade)
        
    if rating == 'C+':
        get_grade += float(grade) * 2.5
        total_grade += float(grade)
        
    if rating == 'C0':
        get_grade += float(grade) * 2.0
        total_grade += float(grade)
        
    if rating == 'D+':
        get_grade += float(grade) * 1.5
        total_grade += float(grade)
        
    if rating == 'D0':
        get_grade += float(grade) * 1.0
        total_grade += float(grade)
        
    if rating == 'F':
        get_grade += 0
    
    # P인 과목은 계산에서 제외
    if rating == 'P':
        continue

# 총합이 0인 경우, 평점도 0점
# 미설정시 zerodivision error
if total_grade == 0:
    avg_grade = 0

# 총합 0 아니면
# 평균 = 획득 학점 / 전체 학점
else:
    avg_grade = get_grade / total_grade

# 소숫점 6자리까지 표현.
print(f'{avg_grade:.6f}')
