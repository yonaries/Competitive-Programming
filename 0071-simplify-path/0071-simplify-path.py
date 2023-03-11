class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        
        stack = deque()
        
        for command in path:
            if command == ".." and stack:
                stack.pop()
                
            elif command and command != ".." and command != ".":
                stack.append("/"+command)
                
        return "".join(stack) if stack else "/" 