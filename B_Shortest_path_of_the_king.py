# def dfs_shortest_path(grid, start, target):
#     # Initialize visited and path arrays
#     visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
#     path = []

#     # Define DFS function
#     def dfs_helper(row, col):
#         # Mark current cell as visited and add to path
#         visited[row][col] = True
#         path.append((row, col))

#         # Check if target cell is reached
#         if (row, col) == target:
#             return True

#         # Explore unvisited neighbors
#         for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
#             if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and not visited[r][c] and grid[r][c] != 1:
#                 if dfs_helper(r, c):
#                     return True

#         # Backtrack by removing last cell from path and marking current cell as unvisited
#         path.pop()
#         visited[row][col] = False
#         return False

#     # Call DFS function from start cell
#     dfs_helper(start[0], start[1])

#     # Return shortest path if target cell is reached, otherwise return None
#     if path and path[-1] == target:
#         return path
#     else:
#         return None

# convert chessboard coordinates to row and column indices
def get_indices(coord):
    col = ord(coord[0]) - ord('a')
    row = int(coord[1]) - 1
    return row, col


# Get input coordinates
s = input().strip()
t = input().strip()

# Get row and column indices for s and t
s_row, s_col = get_indices(s)
t_row, t_col = get_indices(t)

# Calculate horizontal and vertical distances
h_dist = abs(s_col - t_col)
v_dist = abs(s_row - t_row)

# Calculate minimum number of moves
min_moves = max(h_dist, v_dist)

# Print minimum number of moves
print(min_moves)

# Print moves
for i in range(min_moves):
    move = ""
    if s_col < t_col:
        move += "R"
        s_col += 1
    elif s_col > t_col:
        move += "L"
        s_col -= 1

    if s_row < t_row:
        move += "U"
        s_row += 1
    elif s_row > t_row:
        move += "D"
        s_row -= 1
    print(move)
