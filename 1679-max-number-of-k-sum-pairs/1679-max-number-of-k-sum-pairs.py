class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        i = 0
        j = len(nums) - 1
        count = 0
        
        nums.sort()
        
        while i < j:
            if(nums[i] + nums[j] == k):
                count += 1
                i += 1
                j -= 1
                
            elif(nums[i] + nums[j] < k):
                i += 1
                
            else: j -= 1
                
        return count