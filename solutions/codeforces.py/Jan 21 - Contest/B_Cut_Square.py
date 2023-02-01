n = int(input())

for _ in range(n):
    w1, l1 = list(map(int, input().split()))
    w2, l2 = list(map(int, input().split()))

    if (w1+w2) == l1 == l2:
        print("Yes")
    elif (w1+l2) == l1 == w2:
        print("Yes")
    elif (l1+w2) == w1 == l2:
        print("Yes")
    elif (l1+l2) == w1 == w2:
        print("Yes")
    else:
        print("No")
