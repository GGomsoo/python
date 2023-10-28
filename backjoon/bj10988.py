# 팰린드롬인지 확인하기
# 브론즈 III


# 입력받은 단어
word = input()

# 단어 길이를 반틈으로 갈라서 for문 진행
for i in range(len(word)//2):
    # 앞에 단어랑 뒤에 단어랑 다르면
    if word[i] != word[len(word)-1-i]:
        # 0 출력하고 break
        print(0)
        break
# 같은 단어면 = 회문 = 1 출력
else:
    print(1)