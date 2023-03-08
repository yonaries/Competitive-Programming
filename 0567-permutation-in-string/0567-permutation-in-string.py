class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        
        s1_map = {}
        for i in s1:
            s1_map[i] = s1_map.get(i, 0) + 1
        
        l, r = 0, n-1
        
        s2_map = {}
        for i in s2[l:r+1]:
            s2_map[i] = s2_map.get(i, 0) + 1
        
        if s1_map == s2_map:
            return True
            
        while r < len(s2)-1:
            s2_map[s2[l]] -= 1
            
            r += 1
            s2_map[s2[r]] = s2_map.get(s2[r], 0) + 1
            
            if s2_map[s2[l]] == 0:
                del s2_map[s2[l]]
                
            l += 1   
            if s1_map == s2_map:
                return True
        
        return False