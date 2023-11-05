class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        num_list=list(set(nums))
        num_list.sort(reverse=True)
        
        if len(num_list) < 3: return num_list[0]
        else: return num_list[2]