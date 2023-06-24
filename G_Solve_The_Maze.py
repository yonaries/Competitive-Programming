def dfs(maze, visited, x, y):
    if x < 0 or x >= len(maze) or y < 0 or y >= len(maze[0]) or [x][y] == '#' or (x, y) in visited:
        return False
    if maze[x][y] == 'G':
        return True
    visited.add((x, y))
    return dfs(maze, visited, x-1, y) or dfs(maze, visited, x+1, y) or dfs(maze, visited, x, y-1) or dfs(maze, visited, x, y+1)


def solve_maze(maze):
    n, m = len(maze), len(maze[0])
    # Block cells adjacent to bad people
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 'B':
                for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0 <= x < n and 0 <= y < m and maze[x][y] == '.':
                        maze[x][y] = '#'
    # Check if all good people can reach the destination
    visited = set()
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 'G' and not dfs(maze, visited, i, j):
                return "No"
    return "Yes"


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    maze = [list(input().strip()) for _ in range(n)]
    print(solve_maze(maze))
