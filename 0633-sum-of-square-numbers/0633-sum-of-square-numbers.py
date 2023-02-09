class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        low, high = 0, math.floor(math.sqrt(c))

        while low <= high:
            result = low ** 2 + high ** 2
            
            if result == c:
                return True
            elif result > c:
                high -= 1
            else:
                low += 1
                
        return False
            