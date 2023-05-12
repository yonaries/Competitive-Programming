
def fibonacci_army(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci_army(n-1) + fibonacci_army(n-2)


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_army(n))
