n_testcases = int(input())


# def palindrome(arr):
#     return arr == reversed(arr)

def check(arr, left, right, removed):
    while left < right:
        if arr[left] != arr[right]:
            if arr[left] == removed:
                left += 1
            elif arr[right] == removed:
                right += 1
            else:
                return False
        else:
            left += 1
            right += 1


def kalindrome(list):
    left, right = 0, 0


for _ in range(n_testcases):
    n = int(input())
    testcase = list(map(int, input().split()))

    print(kalindrome(testcase))
