class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        counter = 0

        for i in zip(*strs):
            if list(i)!=sorted(i):
                counter+=1

        return counter 
            
        