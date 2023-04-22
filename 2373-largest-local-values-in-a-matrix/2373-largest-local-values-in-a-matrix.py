class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)-2
        result = [[] for _ in range(n)]
        
        for row in range(len(grid)-2):
            for col in range(len(grid)-2):
                
                value = -inf
                for i in range (row, row+3):
                    for j in range(col, col+3):
                        value = max(value,grid[i][j])
                        
                result[row].append(value)
        return result
                    