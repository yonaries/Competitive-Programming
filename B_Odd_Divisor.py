import math


def has_odd_divisor(n):
    if n <= 2:
        return "NO"

    for i in range(1, int(math.sqrt(n))+1, 2):
        if i == 1:
            continue

        if n % i == 0 and i % 2 == 1:  # if i is odd divisor of n
            return "YES"

    # if n is a prime number
    if n % 2 == 1 and n % n == 0:
        return "YES"

    return "NO"


t = int(input())
for i in range(t):
    n = int(input())
    print(has_odd_divisor(n))
