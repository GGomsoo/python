words = input()
lst = ["a", "e", "o", "u", "i"]
ans = 0

for i in lst:
    for w in words:
        if i == w:
            ans += 1

print(ans)