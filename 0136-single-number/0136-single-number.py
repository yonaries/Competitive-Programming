class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = nums[0]
        
        for i in range(1, len(nums)):
            answer = answer ^ nums[i]
            
        return answer
        
        