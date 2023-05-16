class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex <= 1:
            return [1] * (rowIndex + 1)

        return self.compute(1, rowIndex, [1])

    def compute(self, i, rowIndx, array):
        if i == 1:
            return self.compute(i + 1, rowIndx, [1,1])

        newArr = [1] + [0] * (i - 1) + [1]
        for j in range(1, len(array)):
            newArr[j] = array[j] + array[j - 1]
        
        if i == rowIndx:
            return newArr
        return self.compute(i + 1, rowIndx, newArr)
        
        
        