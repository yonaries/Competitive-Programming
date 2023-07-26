class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdic = defaultdict(int)
        tdic = defaultdict(int)
    
        
        for l in s:
            sdic[l] += 1
        
        for l in t:
            tdic[l] += 1
            
        long, short = (sdic, tdic) if len(sdic) > len(tdic) else (tdic, sdic)
            
        for l in long:
            if not short[l] or short[l] != long[l]:
                return False
            
        return True
            