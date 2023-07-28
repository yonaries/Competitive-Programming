class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_rob, prev_rob_2 = 0, 0
        
        for num in nums:
            temp = max(num + prev_rob, prev_rob_2)
            prev_rob = prev_rob_2
            prev_rob_2 = temp
            
        return prev_rob_2