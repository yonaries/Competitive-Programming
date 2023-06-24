def solve():
    n = int(input())
    a = list(map(int, input().split()))
    print(n)
    for i in range(n):
        deg = 1
        while deg < a[i]:
            deg *= 2
        print(i + 1, deg - a[i])
    return 0


def main():
    test_cases = int(input())
    for _ in range(test_cases):
        solve()
    return 0


if __name__ == "__main__":
    main()
