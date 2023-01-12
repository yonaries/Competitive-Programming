class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c = 0
        for ch_s in s: c ^= ord(ch_s)
        for ch_t in t: c ^= ord(ch_t)
        return chr(c)
        