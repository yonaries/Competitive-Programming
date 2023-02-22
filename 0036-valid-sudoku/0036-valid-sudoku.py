class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in board:
            if not self.is_valid(row):
                return False
        # Check columns
        for i in range(9):
            if not self.is_valid([row[i] for row in board]):
                return False
        # Check squares
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not self.is_valid([board[i+k][j+l] for k in range(3) for l in range(3)]):
                    return False
        return True
    
    def is_valid(self, arr):
        arr = [x for x in arr if x != "."]
        return len(arr) == len(set(arr))
    