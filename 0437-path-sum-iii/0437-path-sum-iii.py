# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.result = 0
        cache = {0:1}
        
        self.dfs(root, targetSum, 0, cache)
        
        return self.result
    
    def dfs(self, root, targetSum, currPathSum, cache):
        if root is None:
            return  

        currPathSum += root.val
        oldPathSum = currPathSum - targetSum

        self.result += cache.get(oldPathSum, 0)
        cache[currPathSum] = cache.get(currPathSum, 0) + 1
        
        # dfs breakdown
        self.dfs(root.left, targetSum, currPathSum, cache)
        self.dfs(root.right, targetSum, currPathSum, cache)
        
        cache[currPathSum] -= 1