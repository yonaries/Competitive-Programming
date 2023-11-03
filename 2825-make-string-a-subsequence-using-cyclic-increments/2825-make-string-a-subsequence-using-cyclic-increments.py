class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i = 0
        
        for l in str1:
            if i == len(str2):
                break
                
            if (l == str2[i] or chr(ord(l) + 1) == str2[i] or (l == 'z' and (str2[i] == 'a'))):
                i += 1
            
        return i == len(str2)
                
            
        