class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        window_size = len(needle)
        left = 0
        right = window_size - 1
        
        while right < len(haystack):
            window = haystack[left:right+1]
            
            if window == needle:
                return left
            
            left += 1
            right += 1
        
        return -1