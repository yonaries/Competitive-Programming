class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        nums_set = set()
        
        for i in range(len(nums)):
            val = str(nums[i])[::-1]
            val = int(val)
            
            nums.append(int(val))
            nums_set.add(val)
            nums_set.add(nums[i])
            
        return len(nums_set)