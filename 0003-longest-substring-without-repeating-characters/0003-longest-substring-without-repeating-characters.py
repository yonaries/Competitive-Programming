class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        
        maxLength = 0
        subarray = []
        
        if len(s) == 1:
            return 1
        
        while right < len(s):
            if s[right] in subarray:
                subarray = []
                left += 1
                right = left
            else:
                subarray.append(s[right])
                right += 1
                
            maxLength = max(maxLength, len(subarray))
            
        return maxLength
                