n = int(input())
m = int(input())
a = [int(input()) for i in range(n)]
min_k = max(max(a), (m + sum(a) + n - 1) // n)
max_k = max(a) + m
print(min_k, max_k)
