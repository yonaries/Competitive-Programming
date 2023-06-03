class Solution:
    def minSteps(self, n: int) -> int:
        screen, clipboard, steps = 1, 0, 0
        
        while screen < n:
            if n % screen == 0:
                clipboard = screen
                steps += 1
                
            screen += clipboard
            steps += 1
            
        return steps
        