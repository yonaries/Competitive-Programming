import math

# time complexity: O(sqrt(n))


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True


t = int(input())


# time complexity: O(n*sqrt(n))
for i in range(t):
    n = int(input())
    m = 2  # the smallest prime number that added to n and results a not prime number

    # time complexity: O(n)
    while is_prime(n+m):  # find the smallest prime number that added to n is also prime
        m += 1
    print(m)
