# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def minValue(self, root):
        curr = root
        
        while curr and curr.left:
            curr = curr.left
            
        return curr
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        else:
            # if there isn't left node
            if not root.right:
                return root.left
            
            # if there isn't right node
            elif not root.left:
                return root.right
            
            # if both left and right
            else:
                # find the minimum value
                minNode = self.minValue(root.right)
                
                # replace the curr node val with the minimum value
                root.val = minNode.val
                
                # recursive on right nodes to balance the tree
                root.right = self.deleteNode(root.right, minNode.val)
        
        return root