tc = int(input())

changes = [25, 10, 5, 1] # 잔돈 종류

for i in range(tc):
    money = int(input()) # 거스름돈의 액수
    ans = [0, 0, 0, 0] # 각각 줘야하는 동전의 갯수

    for i in range(4):
        ans[i] += money // changes[i] # 거스름돈을 잔돈으로 나눈 몫 == 갯수를 list에 추가
        money %= changes[i] # 남은 거스름돈
    
    print(*ans)