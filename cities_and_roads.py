n = int(input())
matrix = []

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
res = 0
for i in range(n):
    for j in range(i + 1, n):
        res += matrix[i][j]

print(res)
