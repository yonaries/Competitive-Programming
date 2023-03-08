class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
    
        maxValue = 0
        for i in range(k):
            maxValue += nums[i]
            
        subarray_sum = maxValue
        for i in range(0, len(nums) - k):
            subarray_sum -= nums[i]
            subarray_sum += nums[i + k]
            
            maxValue = max(maxValue, subarray_sum)
        return maxValue / k
            