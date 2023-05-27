# Maruf's approach
t = int(input())

for _ in range(t):
    n = int(input())

    row1 = input().strip()
    row2 = input().strip()
    isReachable = True

    for i in range(n):
        if row1[i] == "1" and row2[i] == "1":
            isReachable = False
            print('NO')
            break

    if isReachable:
        print('YES')


# t = int(input())
# for _ in range(t):
#     n = int(input())

#     row1 = list(map(int, input().strip()))
#     row2 = list(map(int, input().strip()))
#     adjacency = [row1, row2]
#     visited = set()

#     def travel(i, j):
#         if i == 1 and j == n - 1:  # reached the end of the grid
#             return True
#         # out of bounds
#         if i < 0 or i > 1 or j < 0 or j >= n or (i, j) in visited:
#             return False
#         visited.add((i, j))
#         return adjacency[i][j] == 0 and (travel(i, j + 1) or (travel(i + 1, j)) or (travel(i - 1, j)) or travel(i + 1, j + 1)) or travel(i - 1, j + 1)
#     if travel(0, 0):
#         print("YES")
#     else:
#         print("NO")


# t = int(input())

# for _ in range(t):
#     n = int(input())
#     row1 = list(map(str, input().strip()))
#     row2 = list(map(str, input().strip()))
#     grid = [row1, row2]

#     i, j = 0, 0

#     # try to move to cell (2,n) from cell (0,0)
#     while j < n-1:
#         if i == 0:
#             if j+1 < n and grid[i][j+1] == '0':  # right
#                 j += 1

#             elif j+1 < n and grid[i+1][j+1] == '0':  # diagonally down
#                 i, j = i+1, j+1

#             elif grid[i+1][j] == '0':  # down
#                 i += 1

#             else:
#                 break
#         else:
#             if j+1 < n and grid[i][j+1] == '0':  # right
#                 j += 1

#             elif j+1 < n and grid[i-1][j+1] == '0':  # diagonally up
#                 i, j = i-1, j+1

#             elif grid[i-1][j] == '0':  # up
#                 i -= 1

#             else:
#                 break

#     if j == n-1:
#         print("YES")
#     else:
#         print("NO")
