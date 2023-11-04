class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = bin(n)[2:]
        count = 0
        
        for b in bits:
            if b == '1':
                count += 1
                
        return count