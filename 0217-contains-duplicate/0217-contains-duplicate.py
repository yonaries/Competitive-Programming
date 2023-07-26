class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = defaultdict(int)
        
        for num in nums:
            if dic[num]:
                return True
            else:
                dic[num] = 1
                
        return False
            
        
        
        