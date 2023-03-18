class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0] * (len(s) + 1)
        
        for start, end, way in shifts:
            sign = -1 if way == 0 else 1
            prefix[start] += sign
            prefix[end + 1] += -sign
        
        for i in range(1, len(s)):
            prefix[i] += prefix[i - 1]

        shifted = list(s)
        for i in range(len(shifted)):
            val = (ord(shifted[i]) + prefix[i] - 123) % 26 + 97
            shifted[i] = chr(val)
            
        return ''.join(shifted)