class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = []

        for i in range(len(nums)):
            if i == 0:
                output.append(nums[i])
                continue
                
            output.append(output[i-1]+nums[i])
            
        return output 