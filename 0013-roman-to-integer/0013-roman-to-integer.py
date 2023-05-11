class Solution:
    def romanToInt(self, s: str) -> int:
        summation = 0        
        x = 0
        romans = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        

        while x<len(s):
            if x<len(s)-1 and romans[s[x]] < romans[s[x+1]]:
                summation += (romans[s[x+1]] - romans[s[x]])
                x += 2
            else:
                summation += romans[s[x]]
                x += 1
        return summation
        
            
                