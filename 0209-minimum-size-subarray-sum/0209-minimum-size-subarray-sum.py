class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums) == 1 and nums[0] != target:
            return 0
        
        left = 0
        right = 1
        count = float('inf')
        sum = nums[left]
    
        while right < len(nums):
            if nums[right] >= target:
                return 1
            if nums[left] >= target:
                return 1
            sum = sum + nums[right]
            while sum >= target:
                sum = sum - nums[left]
                count = min(count, right - left + 1)
                left += 1
            right += 1
        
        if count == float('inf'):
            return 0
    
        return count