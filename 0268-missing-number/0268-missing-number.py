class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        start, end = 0, len(nums)-1
        answer = -1
        
        while start <= end:
            mid = (start+end)//2
            
            if nums[mid] == mid:
                start = mid+1
                
            else:
                answer = mid
                end = mid-1
            
        return answer if answer != -1 else len(nums)