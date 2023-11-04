class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]
        
        for i in range(len(nums)):
            if len(output) < len(nums):
                output.append(nums[i]*output[i])
        
        postfix = nums[len(nums)-1]
        
        for i in range(len(nums)-2, -1, -1):            
            output[i] *= postfix
            postfix *= nums[i]
            
        return output