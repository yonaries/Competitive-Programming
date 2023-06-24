row, col = list(map(int, input().split()))

matrix = []
for i in range(row):
    matrix.append(list(input()))

directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def inbound(i, j):
    return i >= 0 and i < row and j >= 0 and j < col


def dfs(i, j, parent, visited):
    visited[i][j] = True
    for direction in directions:
        next_i = i + direction[0]
        next_j = j + direction[1]

        if inbound(next_i, next_j) and matrix[next_i][next_j] == matrix[i][j]:
            if (next_i, next_j) == parent and visited[next_i][next_j]:
                return True

            if not visited[next_i][next_j]:
                print((next_i, next_j), parent)
                dfs(next_i, next_j, parent, visited)

    return False


visited = [[False for j in range(col)] for i in range(row)]

for i in range(row):
    for j in range(col):
        if not visited[i][j]:
            cycle = dfs(i, j, (i, j), visited)
            if cycle:
                print("Yes")
                exit()

print("No")
