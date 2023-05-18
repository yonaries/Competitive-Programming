class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        def inBound(row, col):
            if 0 <= row < ROWS and 0 <= col < COLS:
                return True
            return False
        
        visited = set()
        
        def dfs(row, col):
            if not inBound(row, col) or grid[row][col] == 0 or (row, col) in visited:
                return 0
            
            visited.add((row, col))
            return (1 + dfs(row+1, col) + dfs(row-1, col) + dfs(row, col+1) + dfs(row, col-1))
    
        maximum = 0
        for i in range(ROWS):
            for j in range(COLS):
                maximum = max(maximum, dfs(i, j))
                
        return maximum