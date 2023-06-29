t = int(input())

for _ in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)

    for _ in range(q):
        x = int(input())
        total = 0
        count = 0

        for i in range(n):
            if total >= x:
                break
            total += a[i]
            count += 1

        if total >= x:
            print(count)
        else:
            left = 0
            right = n - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if a[mid] >= x - total:
                    ans = mid
                    left = mid + 1
                else:
                    right = mid - 1

            if ans == -1:
                print(-1)
            else:
                print(count + n - ans)
