class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        j = len(s)-1
        
        for i in s:
            if i != s[j]:
                return False
            j-=1
            
        return True