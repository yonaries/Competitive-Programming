class Solution:
    def mySqrt(self, x: int) -> int:
        start, end = 0, x
        answer = 0
        
        
        while start <= end:
            mid = (start+end)//2
            
            if mid * mid <= x:
                answer = mid
                start = mid+1
                
            else:
                end = mid -1
                
        return answer