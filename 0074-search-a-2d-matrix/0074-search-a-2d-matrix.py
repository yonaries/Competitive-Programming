class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
#   -------------------------------------------------------------
#       Approach 1: Binary search aproach
#   -------------------------------------------------------------

#         row_length = len(matrix)
#         column_length = len(matrix[0])
        
#         i = 0
#         j = -1
        
#         while True:
#             if i >= row_length or abs(j) > column_length or target > matrix[row_length-1][column_length-1]:
#                 return False
            
#             if target > matrix[i][j]:
#                 i += 1
#             elif target < matrix[i][j]:
#                 j -= 1
#             else:
#                 return True

    
#   -------------------------------------------------------------
#       Approach 2: loop over rows check if target is a member O(n)
#   -------------------------------------------------------------

        for row in matrix:
            if row[0] > target: 
                return False
            
            elif target in row:
                return True
            
        return False
        