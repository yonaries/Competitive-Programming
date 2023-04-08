# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def constructBST(self, nums, left, right):
        if left >= right: return None
        mid = (left + right)//2
        
        return TreeNode(
            val = nums[mid],
            left = self.constructBST(nums, left, mid),
            right = self.constructBST(nums, mid + 1, right)
        )
                    
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.constructBST(nums, 0, len(nums))
