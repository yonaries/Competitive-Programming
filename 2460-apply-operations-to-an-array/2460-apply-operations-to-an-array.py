class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for i in range(1,len(nums)):
            if nums[i] == nums[i - 1]:
                nums[i-1] *= 2
                nums[i] = 0
                
        output = [x for x in nums if x != 0]
        output += [0] * (len(nums) - len(output))
                
        return output