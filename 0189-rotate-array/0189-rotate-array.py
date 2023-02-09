class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for _ in range(k):
            num = nums.pop()
            nums.insert(0,num)
        