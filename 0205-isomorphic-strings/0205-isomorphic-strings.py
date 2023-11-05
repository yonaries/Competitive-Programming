class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        dic={}
        for i in range(len(s)):
            if not t[i] in dic.values() and not s[i] in dic: dic[s[i]] = t[i]
            elif not s[i] in dic or dic[s[i]] != t[i]: return False
        return True