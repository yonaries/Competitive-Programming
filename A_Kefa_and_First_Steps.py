

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))

    ans = 1
    mx = 1

    for i in range(1, n):
        if a[i] >= a[i - 1]:
            ans += 1
            mx = max(ans, mx)
        else:
            ans = 1
    print(mx)
