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
            
            lh = helper(node.left)
            rh = helper(node.right)
            
            if p == node or q == node or (lh and rh):
                return node
            
            if lh or rh:
                return lh or rh
            
            return None
        
        
        return helper(root)