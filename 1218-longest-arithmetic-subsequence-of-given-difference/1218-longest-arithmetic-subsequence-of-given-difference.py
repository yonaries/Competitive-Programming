class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}  # Stores the maximum length at each index
        
        ans = 1 
        
        for num in arr:
            if num - difference in dp:
                dp[num] = 1 + dp[num - difference]
            else:
                dp[num] = 1
            
            ans = max(ans, dp[num])
        
        return ans
    
    # 1: 1
    # 5: 1
    # 7: 2
    # 8: 1
    # 3: 2
    # 4: 1
    # 2: 1
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    