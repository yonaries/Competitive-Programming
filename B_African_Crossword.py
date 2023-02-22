n, m = map(int, input().split())

grid = []
for i in range(n):
    grid.append(list(input()))

ans = ""

for i in range(n):
    for j in range(m):
        flag = False
        for k in range(n):
            if (i != k and grid[i][j] == grid[k][j]):
                flag = True
        for l in range(m):
            if (j != l and grid[i][j] == grid[i][l]):
                flag = True
        if (not flag):
            ans += grid[i][j]

if (ans == ""):
    print("No solution!")
else:
    print(ans)
