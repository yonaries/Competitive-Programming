class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums.sort()
        
        visited = {}
        
        for index, value in enumerate(nums):
            remainder = target - value
            
            if remainder in visited:
                return [index, visited[remainder]]
            
            visited[value] = index