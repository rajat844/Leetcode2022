# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root :
            return root
        
        def helper(root):
            if root == None:
                return None
            
            lch = helper(root.left)
            rch = helper(root.right)
            
            if (lch != None and rch != None) or root == p or root == q:
                return root
            
            else:
                return lch or rch 
            
        return helper(root)
        