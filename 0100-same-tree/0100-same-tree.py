# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not q and not p:
            return True
        
        if not q or not p:
            return False
        
        if p.val == q.val:
            p_result = self.isSameTree(p.left, q.left)
            q_result = self.isSameTree(p.right, q.right)
            
            return p_result and q_result
        
        return False