class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        me = 0
        piles.sort()
        
        j = len(piles)-2
        i = 0
        
        while i < j:
            me += piles[j]
            i+=1
            j -= 2
        
        return me