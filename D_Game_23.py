import math

n, m = map(int, input().split())

if m % n != 0:
    print(-1)

else:
    x = m // n
    moves = 0
    while x % 2 == 0:
        x //= 2
        moves += 1
    while x % 3 == 0:
        x //= 3
        moves += 1
    if x == 1:
        print(moves)
    else:
        print(-1)
