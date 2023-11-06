# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def traverse(node):
            if not node: return False
            if not node.val in dic: dic[k-node.val]=1
            else: return True
            return traverse(node.left) or traverse(node.right)
        
        dic={}
        return traverse(root)