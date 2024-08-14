lst = list(range(1, 21)) # 1부터 20까지의 숫자카드

for _ in range(10): # 10줄에 걸친 구간
    a, b = map(int, input().split()) # 구간에 대한 숫자

    for i in range((b-a+1) // 2): # (끝 구간 - 시작 구간 + 1) // 2 한 만큼만 반복문을 하면 된다 
        lst[a+i-1], lst[b-i-1] = lst[b-i-1], lst[a+i-1] # -1 을 한 이유는 인덱스값 때문

print(*lst)