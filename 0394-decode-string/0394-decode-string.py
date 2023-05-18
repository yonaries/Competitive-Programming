class Solution:
    def trans(self, s:str, q):
        print(s, q)
        N = len(s)
        ptr = 0
        curr_string = ""
        curr_num = ""
        
        while ptr < N:
            c = s[ptr]

            if c.isnumeric():
                curr_num += c
                
            elif c == '[':

                m = int(curr_num)
                end = q.popleft()
                
                curr_string +=  m * self.decodeString(s[ptr+1:end])
                ptr = end 
                curr_num = ""
                
            elif c != ']':
                curr_string += c
                 
            ptr += 1
        return curr_string
            
    def decodeString(self, s: str) -> str:
        q = deque()
        stack = deque()

        N = len(s)

        for i in range(N):
            if s[i] == '[':
                stack.append(i)
            
            elif s[i] == ']':
                stack.pop()
                if len(stack) == 0:
                    q.append(i)

        return self.trans(s, q)
        

        
            
            
        