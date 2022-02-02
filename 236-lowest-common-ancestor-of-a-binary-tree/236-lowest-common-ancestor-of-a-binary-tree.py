# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def helper(root):
            if root is None:
                return 0
            
            x = helper(root.left)
            y = helper(root.right)
            
            if (x and y) or (root.val == p.val or root.val == q.val):
                return root
            
            elif (x or y):
                return (x or y)
            else :
                return None
        
        ans = helper(root)
        return ans