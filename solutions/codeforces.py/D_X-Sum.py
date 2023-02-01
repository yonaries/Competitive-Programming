"""
         0 1 2 3
    
    1 2 2 1
    1    2 4 2 4
    2    2 2 3 1
    3    2 4 2 4
    
    # main
    {0: 5, -1: 4, -2: 2, -3: 1, 1: 2} {r-c: sum} 
    
    # other
    {0: 1, 1: 2, 2: 4, 3: 3, 1: 2} {r+c: sum} 
    
    (0, 0), (1, 1), (2, 2), (3, 3)  dif = 0
    (0, 3), (1, 2), (2, 1), (3, 0)  sum = 3
"""


def findWinner(grid):
    main = {}
    cross = {}
    n, m = len(grid), len(grid[0])

    # pre-computing
    for r in range(n):
        for c in range(m):
            main[r-c] = grid[r][c] + main.get(r-c, 0)
            cross[r+c] = grid[r][c] + cross.get(r+c, 0)

    ans = 0

    for r in range(n):
        for c in range(m):
            total_sum = main[r-c] + cross[r+c] - grid[r][c]
            ans = max(ans, total_sum)

    return ans


t = int(input())
for _ in range(t):
    n, m = [int(i) for i in input().split()]
    grid = []
    for i in range(n):
        grid.append([int(j) for j in input().split()])

    print(findWinner(grid))
