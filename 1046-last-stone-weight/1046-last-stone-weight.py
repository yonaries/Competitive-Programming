class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            y = stones.pop(stones.index(max(stones)))
            x = stones.pop(stones.index(max(stones)))
            
            # If the stone weights are different, replace with the difference. 
            if x != y:
                stones.append(y - x)
        
        if len(stones) == 0:
            return 0
        
        else:
            return stones[0]