
def numMagicSquaresInside(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    count = 0
    for i in range(len(grid) - 2):
        for j in range(len(grid[0]) - 2):
            if grid[i + 1][j + 1] != 5:
                continue
            if 15 == sum(grid[i][j:j + 3]) == sum(grid[i + 2][j:j + 3]) == sum(grid[k][j] for k in (i, i + 1, i + 2)) == sum(grid[k][j + 2] for k in (i, i + 1, i + 2)):
                if len(set(grid[i][j:j + 3] + grid[i + 1][j:j + 3] + grid[i + 2][j:j + 3])) == 9:
                    count += 1
    return count


grid = [[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]
print(numMagicSquaresInside(grid))
