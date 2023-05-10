class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = '{:032b}'.format(x)
        y = '{:032b}'.format(y)
        
        count = 0
        for i in range(32):
            if int(x[i]) ^ int(y[i]):
                count += 1
                
        return count