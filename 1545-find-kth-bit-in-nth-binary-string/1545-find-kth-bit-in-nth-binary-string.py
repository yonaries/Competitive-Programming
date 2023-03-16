class Solution:
    def invert(self, s):
        value = ""
        
        for char in s:
            if char == '0':
                value = value + "1"
            else:
                value = value + "0"
                
        return value
        
    def findKthBit(self, n: int, k: int) -> str:
         
        def compute(n, s):
            if n == 0:
                return s
            
            inverted = self.invert(s.strip())
            output = s + "1" + inverted[::-1]
            
            return compute(n-1, output)
        
        result = compute(n, "0")
        
        return result[k-1]