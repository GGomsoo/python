tc = int(input())

for _ in range(tc):
    math = list(map(str, input().split()))
    number = float(math[0])

    for i in range(1, len(math)):
        if math[i] == "@":
            number *= 3
        if math[i] == "%":
            number += 5
        if math[i] == "#":
            number -= 7
    
    print(f"{number:.2f}")