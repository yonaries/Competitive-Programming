class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result = []

        for i in range(len(matrix[0])):
            arr = []
            for j in range(len(matrix)):
                arr.append(matrix[j][i])
            result.append(arr)
        return result
                
        