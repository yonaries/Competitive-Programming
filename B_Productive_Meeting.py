# def max_talks(t, test_cases):
#     results = []
#     for case in test_cases:
#         n, a = case
#         talks = []
#         while True:
#             # Find the two persons with the highest sociability
#             max1, max2 = sorted(range(n), key=lambda i: a[i], reverse=True)[:2]
#             if a[max1] == 0 or a[max2] == 0:
#                 break
#             talks.append((max1 + 1, max2 + 1))
#             a[max1] -= 1
#             a[max2] -= 1
#         results.append((len(talks), talks))
#     return results


# # Example input
# t = int(input())
# test_cases = []

# for _ in range(t):
#     desc = int(input())
#     arr = list(map(int, input().split()))
#     test_cases.append((desc, arr))

# # Solve and print the output
# output = max_talks(t, test_cases)
# for k, talks in output:
#     print(k)
#     for i, j in talks:
#         print(i, j)
