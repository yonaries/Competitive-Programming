class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = deque()
        
        speed_time = [(x,y) for x,y in zip(position,speed)]
        speed_time.sort()
        
        for (pos, velocity) in speed_time:
            
            time = (target-pos)/velocity
            
            while stack and stack[-1] <= time:
                stack.pop()
                    
            stack.append(time)
            
        return len(stack)