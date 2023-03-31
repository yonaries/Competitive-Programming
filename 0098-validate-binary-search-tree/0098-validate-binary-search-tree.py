# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def validate(self, root, minT, maxT):
        if not root:
            return True
        
        # if not (root.val <= maxT and root.val >= minT):
        if minT >= root.val or root.val >= maxT:
            return False
        
        left = self.validate(root.left, minT, root.val)
        right = self.validate(root.right, root.val, maxT)
        
        return left and right
        
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        minT = -inf
        maxT = inf
        
        return self.validate(root, minT, maxT)