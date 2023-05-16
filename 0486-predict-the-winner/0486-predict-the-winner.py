class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:

        def predict(left, right):
            if left == right:
                return nums[left]

            from_left = nums[left] - predict(left + 1, right)
            from_right = nums[right] - predict(left, right - 1)

            return max(from_left, from_right)
            
        return predict(0, len(nums) - 1) >= 0