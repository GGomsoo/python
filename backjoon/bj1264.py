while True:
    words = input().lower() # 입력받는 문구를 모두 소문자로 변경
    moem = ["a", "e", "o", "u", "i" ] # 찾아야햐는 모음 리스트
    ans = 0 # 모음 개수

    if words == "#": # 입력에 # 이 들어오면 while문 멈춤
        break

    else:
        for m in moem: 
            for w in words:
                if m == w:
                    ans += 1
        print(ans)