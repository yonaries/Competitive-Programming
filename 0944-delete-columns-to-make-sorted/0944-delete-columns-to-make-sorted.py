class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        counter = 0

        for i in zip(*strs):
            if list(i)!=sorted(i):
                counter+=1

        return counter
    
#   ---------------------------
#       Brute force Approach
#   ---------------------------
#         count = 0
        
#         for i in range(len(strs[0])):
#             column = [ord(line[i])for line in strs]
            
#             if column != sorted(column):
#                 count += 1
        
#         return count
            
        