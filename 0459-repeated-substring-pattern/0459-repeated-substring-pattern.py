class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        new_s=(s+s)[1:-1]
        return s in new_s