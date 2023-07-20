# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rootToLeafPathSum(self, root: TreeNode, targetSum: int, sum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None:
            sum += root.val
            if sum == targetSum:
                return True   
        return self.rootToLeafPathSum(root.left, targetSum, sum + root.val) or self.rootToLeafPathSum(root.right, targetSum, sum + root.val)

    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        sum = 0
        return self.rootToLeafPathSum(root, targetSum, sum)
        