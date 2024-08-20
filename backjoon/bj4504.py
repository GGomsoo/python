N = int(input())

while True:
    a = int(input())

    if a == 0:
        break

    else:
        if a % N == 0:
            print(f"{a} is a multiple of {N}.")
        else:
            print(f"{a} is NOT a multiple of {N}.")