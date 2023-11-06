class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        num_counts = Counter(nums)
    
        duplicates = [num for num, count in num_counts.items() if count == 2]
    
        n = len(nums)
        missing = [i for i in range(1, n + 1) if i not in num_counts]
    
        return duplicates + missing