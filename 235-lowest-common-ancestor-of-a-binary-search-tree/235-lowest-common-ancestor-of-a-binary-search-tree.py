# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def helper(node):
            if node is None:
                return None
            
            if node == p or node == q:
                return node
            
            lh = helper(node.left)
            rh = helper(node.right)
            
            if lh != None and rh!= None:
                return node
            
            if lh != None or rh!= None:
                return lh or rh
            
            return None
        
        ans = helper(root)
        return ans
            
            