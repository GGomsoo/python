# 단어 공부
# 브론즈 I
# 입력받은 단어 중 가장 많이 사용된 알파벳 찾아내기

# 입력받는 단어 전부 대문자 처리
word = input().upper()

# A부터 Z까지 사용횟수 관리할 리스트
abc_cnt = [0] * 26
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# 초기 idx값 0으로 설정
idx = 0
for i in word:
    # i가 알파벳 안에 있다면
    if i in alphabet:
        # idx = 알파벳에서 i에 해당하는 값의 인덱스로 설정
        idx = alphabet.index(i)
        # 사용횟수 리스트에 해당 인덱스값에 횟수 누적
        abc_cnt[idx] += 1

# 많이 사용한 단어가 2개 이상이면 '?' 출력
if abc_cnt.count(max(abc_cnt)) >= 2:
    print('?')

# 많이 사용한 단어가 1종류라면
# 사용횟수 리스트에서 최대값에 대한 인덱스값을 알파벳의 인덱스값으로 사용
# 많이 사용한 단어를 출력
else:
    print(alphabet[abc_cnt.index(max(abc_cnt))])