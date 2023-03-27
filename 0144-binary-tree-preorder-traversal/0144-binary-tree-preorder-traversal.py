# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.inorder = []
        
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if root:
            self.inorder.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
            
        return self.inorder