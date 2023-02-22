n_testcases = int(input())


def remove_smallest(arr, length):
    arr.sort()
    for i in range(length - 1):
        if arr[i + 1] - arr[i] > 1:
            return "NO"
    return "YES"


for _ in range(n_testcases):
    length = int(input())
    arr = list(map(int, input().split()))
    print(remove_smallest(arr, length))
