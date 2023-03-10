class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = deque()
        
        for command in logs:
            if command == "./":
                continue
            elif command == "../":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(command)
                
        return len(stack)