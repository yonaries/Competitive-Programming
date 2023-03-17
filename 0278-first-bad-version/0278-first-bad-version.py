# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start, end = 1, n
        
        answer = 0
        
        while start <= end:
            mid = (start + end) // 2
            
            if not isBadVersion(mid):
                start = mid + 1
                
            else:
                answer = mid
                end = mid - 1
            
        return answer