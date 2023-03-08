class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        window = [0] * 26
        left = 0
        result = 0
        maxFreq = 0
        
        for right in range(n):
            window[ord(s[right])-65] += 1
            windowSize = right - left + 1
            maxFreq = max(maxFreq,window[ord(s[right])-65]) 
            
            if windowSize - maxFreq > k:
                window[ord(s[left])-65] -= 1
                left += 1
            
        return right - left + 1