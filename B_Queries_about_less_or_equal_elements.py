def firstLessNumber(array: list, target: int) -> int:
    left = 0
    right = len(array) - 1

    index = -1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
            index = mid
    return index + 1 if (index > -1) else 0


n, m = map(int, input().split())
list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))

list_a.sort()
for i in range(m):
    print(firstLessNumber(list_a, list_b[i]), end=' ')
