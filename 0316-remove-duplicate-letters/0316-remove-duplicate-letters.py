class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        occur = {c: i for i, c in enumerate(s)}
        stack = []
        visited = set()
        
        for i, char in enumerate(s):
            if char not in visited:
                while stack and stack[-1] > char and occur[stack[-1]] > i:
                    last = stack.pop()
                    visited.remove(last)
                stack.append(char)
                visited.add(char)

        return ''.join(stack)