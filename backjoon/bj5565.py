total = int(input())
another_book = 0

for _ in range(9):
    book = int(input())
    another_book += book

ans = total - another_book
print(ans)