class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        word1_queue = deque()
        word2_queue = deque()
        
        merged = []
        
        for letter in word1:
            word1_queue.append(letter)
            
        for letter in word2:
            word2_queue.append(letter)
            
            
        while word1_queue and word2_queue:
            if word1_queue >= word2_queue:
                letter = word1_queue.popleft()
                merged.append(letter)
            
            else:
                letter = word2_queue.popleft()
                merged.append(letter)
        
        if word1_queue:
            merged.extend(word1_queue)
            
        elif word2_queue:
            merged.extend(word2_queue)
        
        return "".join(merged)