class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        l = []
        
        for i in range(1,len(nums)):
            if nums[i] == nums[i - 1]:
                nums[i-1] *= 2
                nums[i] = 0
                
            if nums[i-1] != 0:
                l.append(nums[i-1])
                
            if i == len(nums)-1 and nums[len(nums)-1] != 0:
                l.append(nums[i])
            
                
            
        for i in range(len(nums) - len(l)):
            l.append(0)
                
        return l