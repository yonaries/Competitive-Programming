n = int(input())
nums = list(map(int, input().split()))
states = input()


def solve(n, nums, states):
    maxi = 0

    for i in range(n-1):
        maxi = max(maxi, nums[i])
        if states[i] == '0' and maxi > i+1:
            return 'NO'
    return 'YES'


print(solve(n, nums, states))


# def isSwapPossible(n, nums, states):
#     for i in range(n-1):
#         if (nums[i] > nums[i+1] and states[i] == 0) or (i > 0 and nums[i] < nums[i-1]):
#             return 'NO'

#         if nums[i] <= nums[i+1]:
#             continue

#         nums[i], nums[i+1] = nums[i+1], nums[i]

#     return 'YES'


# print(isSwapPossible(n, nums, states))


# def can_sort(n, a, states):
#     for i in range(n - 1):
#         if states[i] == '1':
#             min_val, max_val = min(a[i], a[i + 1]), max(a[i], a[i + 1])
#             a[i], a[i + 1] = min_val, max_val

#     return a == sorted(a)


# # Read input
# n = int(input())
# a = list(map(int, input().split()))
# states = input()

# # Check if the array can be sorted
# if can_sort(n, a, states):
#     print("YES")
# else:
#     print("NO")

# n = int(input())
# a = list(map(int, input().split()))
# s = input()
# x = -1

# for i in range(n-1):
#     if s[i] == '0':
#         if x == -1:
#             l = 0
#         else:
#             l = x + 1

#         r = i

#         for j in range(l, r+1):
#             if a[j] >= l+1 and a[j] <= r1:
#                 continue
#             else:
#                 print("NO")
#                 exit()

#         x = i

# print("YES")
