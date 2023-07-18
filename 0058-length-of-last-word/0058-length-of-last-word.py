class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        *rest, last = s
        
        return len(last)