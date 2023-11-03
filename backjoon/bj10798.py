# 세로읽기
# 브론즈 I

# 단어 총 갯수
N = 5

# 단어 5개 입력
words = [input() for _ in range(N)]

# 단어의 갯수로 for문 돌릴게 아니라
# 단어 길이 제일 긴거를 기준으로 돌려서 조건을 더 입력해야함
for i in range(N):
    word = ''
    for j in range(N):
        word += words[j][i]

    print(word, end='')


# 1차 실패