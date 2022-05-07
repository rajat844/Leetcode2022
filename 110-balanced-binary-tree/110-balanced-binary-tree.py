# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(node):
            if node is None:
                return 0
            lh = helper(node.left)
            rh = helper(node.right)
            
            if abs(lh - rh) > 1 or lh == -1 or rh == -1:
                return -1
            else :
                return max(lh,rh) + 1
        
        if helper(root) == -1:
            return False
        return True
        