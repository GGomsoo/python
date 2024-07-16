N = int(input())
num = 1
cnt = 0

for i in range(1, N+1):
    num *= i

for i in range(len(str(num))-1, 0, -1):
    if str(num)[i] == "0":
        cnt += 1
    else:
        break
print(cnt)
