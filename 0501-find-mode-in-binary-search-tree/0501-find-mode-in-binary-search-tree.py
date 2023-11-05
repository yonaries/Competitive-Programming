# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(node):
            if node: 
                dic[node.val]+=1 
                traverse(node.left)
                traverse(node.right)
            
        dic = Counter()
        traverse(root)
        
        mx=max(dic.values(),default=0)
        
        keys = []
        for k, v in dic.items():
            if v==mx: keys.append(k)
                
        return keys