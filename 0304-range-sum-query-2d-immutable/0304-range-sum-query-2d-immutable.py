class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        prefixSum = [[0] * (len(matrix[0])+1)  for x in range(len(matrix)+1)]
       
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 and j == 0:
                    prefixSum[i+1][j+1] = matrix[i][j]
                elif i == 0:
                    value = prefixSum[i+1][j] + matrix[i][j]
                    prefixSum[i+1][j+1] = value
                elif j == 0:
                    value = prefixSum[i][j+1] + matrix[i][j]
                    prefixSum[i+1][j+1] = value
                else:
                    value = (prefixSum[i+1][j] + prefixSum[i][j+1]  + matrix[i][j]) - prefixSum[i][j]
                    prefixSum[i+1][j+1] = value
        
        self.prefixSum = prefixSum

      
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        x = self.prefixSum[row2+1][col1]
        y = self.prefixSum[row1][col2+1]
        z = self.prefixSum[row1][col1]
        result = (self.prefixSum[row2+1][col2+1] - x - y) + z
        return result