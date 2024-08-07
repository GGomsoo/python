tc = int(input())

changes = [25, 10, 5, 1]

for i in range(tc):
    money = int(input())

    while money == 0:
        ans = [0, 0, 0, 0]

        for i in range(len(ans)):
            ans += money // changes[i]
            money %= changes[i]
        print(*ans, end=" ")