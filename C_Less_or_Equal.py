n, k = map(int, input().split())


def less_or_equal(arr, k, length):
    count = 0
    arr.sort()

    for i in range(length):
        if arr[i] <= k:
            count += 1
        else:
            break

    return count if count != 0 else -1


arr = list(map(int, input().split()))
print(less_or_equal(arr, k, n))

# 1, 3, 3, 5, 7, 10, 20
