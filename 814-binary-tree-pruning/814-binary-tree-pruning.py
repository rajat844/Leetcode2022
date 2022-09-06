# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node):
            if node is None:
                return
            lh = helper(node.left)
            rh = helper(node.right)
            
            if lh == None:
                node.left = None
            if rh == None:
                node.right = None
            
            if rh or lh or node.val == 1:
                return node
            else:
                return None
            
        return helper(root)
        