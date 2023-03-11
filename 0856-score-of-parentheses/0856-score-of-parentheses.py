class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        
        for par in s:
            if par == "(":
                stack.append(0)
            else:
                last_score = stack.pop()
                
                # if the last score is 0, then we just closed a pair of parentheses
                if last_score == 0:
                    stack[-1] += 1
                    
                # if the last score is not 0, then we just closed a balanced parentheses string
                else:
                    stack[-1] += 2*last_score
                    
        return stack.pop()