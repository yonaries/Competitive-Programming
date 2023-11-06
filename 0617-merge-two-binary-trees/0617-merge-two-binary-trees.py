# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> Optional[TreeNode]:
        if t1 and t2:
            root, root.left, root.right = TreeNode(t1.val + t2.val), self.mergeTrees(t1.left, t2.left), self.mergeTrees(t1.right, t2.right)
            return root
        else: return t1 or t2