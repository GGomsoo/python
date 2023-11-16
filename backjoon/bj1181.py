# 단어 정렬
# 실버 V

# 소문자로 이루어진 N개의 단어 들어오면
# 1. 길이가 짧은 것 부터
# 2. 길이가 같다면 사전 순으로

N = int(input())
words = []

for _ in range(N):
    word = input()
    words.append(word)

# 중복 제거
# 리스트 형태가 아닌 '{}' 형태
set_words = set(words)

# 중복 제거한 객체를 다시 리스트화
ans = list(set_words)

# 사전 순서대로 정렬
ans.sort()

# 다시 길이순으로 정렬
ans.sort(key=len)

# ans내에 요소들 출력
for word in ans:
    print(word)
