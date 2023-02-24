n_testcases = int(input())


def kalindrome(arr):
    left = 0
    right = len(arr) - 1
    removed = 0
    while left < right:
        if arr[left] != arr[right]:
            if arr[left] == removed:
                left += 1
            elif arr[right] == removed:
                right -= 1
            else:
                return "NO"
        else:
            left += 1
            right -= 1
    return "YES"


for _ in range(n_testcases):
    n = int(input())
    testcase = list(map(int, input().split()))

    print(kalindrome(testcase))
