import math
n, k = input().split()
k = int(k)
n = int(n)

count = 0
scores = list(map(int, input().split()))
threshold = scores[k]

for i in range(0, n):
    if scores[i] < threshold or scores[i] == 0:
        break

    elif scores[i] >= threshold:
        count += 1


print(count)
