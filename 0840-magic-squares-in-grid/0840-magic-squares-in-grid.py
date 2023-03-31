class Solution:
    def isMagicalGrid(self, row: int, col: int, grid: List[List[int]]) -> bool:
        elements = set()

        for i in range(3):
            for j in range(3):
                if 1 <= grid[row + i][col + j] <= 9:
                    elements.add(grid[row + i][col + j])
            
        if len(elements) < 9:
            return False
            
        firstSum = sum(grid[row][col: col + 3])
        if sum(grid[row + 1][col: col+3]) != sum(grid[row + 2][col: col+3]) != firstSum:
            return False
            
        for i in range(3):
            curRowSum = 0
            for j in range(3):
                curRowSum += grid[row + j][col + i]
            if curRowSum != firstSum:
                return False
                
        for i in range(2):
            diagonalSum = 0
            for j in range(3):
                diagonalSum += grid[row + j][col + j]
            if diagonalSum != firstSum:
                return False
            
        return True
    
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0
            
        count = 0
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                if self.isMagicalGrid(i, j, grid):
                    count += 1
        
        return count