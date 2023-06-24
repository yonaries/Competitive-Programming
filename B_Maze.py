n, m, k = list(map(int, input().split()))

matrix = []
for i in range(n):
    line = list(input())
    matrix.append(line)


def inbound(r, c):
    if r > n or r < 0 or c < 0 or c > m:
        return False
    return True


def isLeaf(i, j):
    blocks = 0
    if not inbound(i - 1, j) or matrix[i - 1][j] == "#" or matrix[i - 1][j] == "X" or not inbound(i + 1, j) or matrix[i + 1][j] == "#" or matrix[i + 1][j] == "X" or not inbound(i, j-1) or matrix[i][j-1] == "#" or matrix[i][j+1] == "X" or not inbound(i, j-1) or matrix[i][j-1] == "#" or matrix[i][j-1] == "X":
        blocks += 1

    return True if blocks == 3 else False


def dfs(i, j):
    if isLeaf(i,matrix j):
        print('leaf')
        matrix[i][j] = "X"
        return

    if inbound(i-1, j) and matrix[i-1][j] == '.':
        return dfs(i-1, j)

    if inbound(i+1, j) and matrix[i+1][j] == '.':
        return dfs(i+1, j)

    if inbound(i, j-1) and matrix[i][j - 1] == '.':
        return dfs(i, j-1)

    if inbound(i, j+1) and matrix[i][j+1] == '.':
        return dfs(i, j+1)

    return


def solve():
    for i in range(n):  # find the first node of the connected component
        for j in range(m):
            if matrix[i][j] == ".":
                dfs(i, j)  # run a dfs
                return


solve()
for line in matrix:
    print(''.join(line))
