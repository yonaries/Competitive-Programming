def dfs(maze, visited, x, y, n, m, k):
    if k[0] == 0:
        return

    visited[x][y] = True
    k[0] -= 1

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maze[nx][ny] == '.':
            dfs(maze, visited, nx, ny, n, m, k)


# Read input
n, m, k = map(int, input().split())
maze = [list(input()) for _ in range(n)]

# Find the starting point
for i in range(n):
    for j in range(m):
        if maze[i][j] == '.':
            start_x, start_y = i, j
            break

# Perform DFS traversal
visited = [[False] * m for _ in range(n)]
dfs(maze, visited, start_x, start_y, n, m, [k])

# Mark visited cells as "X" and print the modified maze
for i in range(n):
    for j in range(m):
        if visited[i][j]:
            maze[i][j] = 'X'
    print(''.join(maze[i]))
