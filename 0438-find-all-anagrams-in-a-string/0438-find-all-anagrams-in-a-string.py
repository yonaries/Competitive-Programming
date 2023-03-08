class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = dict(Counter(p))
        left = 0
        right = len(p) - 1
        
        dict_win = dict(Counter(s[left: right + 1]))
        ans = []
        
        while right < len(s):
            if dict_win == target:
                ans.append(left)
                
            val = s[left]
            if dict_win[val] == 1:
                del dict_win[val]
                
            else:
                dict_win[val] -= 1
                
            val = s[right + 1] if right + 1 < len(s) else ''
            dict_win[val] = dict_win.get(val, 0) + 1
            right += 1
            left += 1
            
        if dict_win == target:
            ans.append(left - 1)
            
        return ans