# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.result = []
        def traverse(root):
            if not root:
                return None
            
            tree_nodes = findSumDFS(root, [])
            if root.val == sum(tree_nodes)//len(tree_nodes):
                self.result.append(root.val)

            if root.left:
                traverse(root.left)
            
            if root.right:
                traverse(root.right)


        def findSumDFS(root, tree_nodes):
            if not root:
                return None
            
            tree_nodes.append(root.val)

            if root.left:
                findSumDFS(root.left, tree_nodes)
            
            if root.right:
                findSumDFS(root.right, tree_nodes)
            
            return tree_nodes
        
        traverse(root)
        return len(self.result)
        